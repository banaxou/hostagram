import contextlib
import importlib.util
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch


SOURCE = Path(__file__).resolve().parents[1] / "hostagram.py"


def load_hostagram():
    spec = importlib.util.spec_from_file_location("hostagram_under_test", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        original_dir = Path.cwd()
        os.chdir(self.temp_dir.name)
        self.addCleanup(os.chdir, original_dir)

        self.output = io.StringIO()
        self.enterContext(contextlib.redirect_stdout(self.output))
        self.clear_screen = self.enterContext(patch("os.system", return_value=0))
        self.enterContext(patch("time.sleep"))
        # Import must never prompt, clear the screen, or truncate a saved session.
        with patch("builtins.input", side_effect=AssertionError("Import prompted for input")):
            self.app = load_hostagram()

    def test_import_has_no_interactive_side_effects(self):
        Path("sessionid.txt").write_text("existing-session", encoding="utf-8")
        with patch("builtins.input", side_effect=AssertionError("Import prompted for input")):
            load_hostagram()
        self.clear_screen.assert_not_called()
        self.assertEqual(self.output.getvalue(), "")
        self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "existing-session")
        self.assertFalse(Path("user.txt").exists())

    def test_password_login_passes_username_as_one_argument(self):
        username = "example & echo shell-marker"
        Path("sessionid.txt").write_text("existing-session", encoding="utf-8")
        with patch("builtins.input", side_effect=["p", username]), patch.object(
            self.app.subprocess, "run"
        ) as run, patch.object(self.app.os, "remove") as remove:
            self.app.login_easy()

        run.assert_called_once_with(
            [sys.executable, "-m", "instaloader", "--login", username], check=True
        )
        remove.assert_not_called()
        self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "")
        self.assertEqual(Path("user.txt").read_text(encoding="utf-8"), username + "\n")
        self.assertTrue(all("shell-marker" not in call.args[0] for call in self.clear_screen.call_args_list))

    def test_failed_password_login_retries_without_recording_failed_user(self):
        errors = [subprocess.CalledProcessError(1, "instaloader"), OSError("Cannot start process")]
        for error in errors:
            with self.subTest(error=type(error).__name__):
                Path("user.txt").write_text("known-user\n", encoding="utf-8")
                Path("sessionid.txt").write_text("existing-session", encoding="utf-8")
                with patch("builtins.input", side_effect=["p", "failed-user", "p", "good-user"]), patch.object(
                    self.app.subprocess, "run", side_effect=[error, Mock(returncode=0)]
                ) as run:
                    self.app.login_easy()

                self.assertEqual(run.call_count, 2)
                self.assertEqual(Path("user.txt").read_text(encoding="utf-8"), "known-user\ngood-user\n")
                self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "")
                self.assertIn("Login failed", self.output.getvalue())

    def test_failed_password_login_preserves_session_when_cancelled(self):
        Path("sessionid.txt").write_text("existing-session", encoding="utf-8")
        with patch("builtins.input", side_effect=["p", "example", KeyboardInterrupt]), patch.object(
            self.app.subprocess, "run", side_effect=subprocess.CalledProcessError(1, "instaloader")
        ), self.assertRaises(KeyboardInterrupt):
            self.app.login_easy()
        self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "existing-session")
        self.assertFalse(Path("user.txt").exists())

    def test_empty_username_is_rejected_before_starting_login(self):
        with patch("builtins.input", side_effect=["p", "  ", "p", "example"]), patch.object(
            self.app.subprocess, "run"
        ) as run:
            self.app.login_easy()
        self.assertEqual(run.call_count, 1)
        self.assertIn("Empty username", self.output.getvalue())

    def test_existing_username_is_not_duplicated(self):
        Path("user.txt").write_text("example\n", encoding="utf-8")
        with patch("builtins.input", side_effect=["p", "example"]), patch.object(
            self.app.subprocess, "run"
        ):
            self.app.login_easy()
        self.assertEqual(Path("user.txt").read_text(encoding="utf-8"), "example\n")

    def test_invalid_menu_choice_preserves_saved_session(self):
        Path("sessionid.txt").write_text("existing-session", encoding="utf-8")
        with patch("builtins.input", side_effect=["invalid", KeyboardInterrupt]), self.assertRaises(KeyboardInterrupt):
            self.app.login_easy()
        self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "existing-session")
        self.assertIn("Invalid choice", self.output.getvalue())

    def test_session_login_hides_secret_and_saves_it_after_success(self):
        with patch("builtins.input", side_effect=["s", "example"]), patch.object(
            self.app.getpass, "getpass", return_value="new-session-secret"
        ) as secret_prompt, patch.object(self.app.instaloader, "Instaloader"), patch.object(
            self.app.instaloader.Profile, "from_username", return_value=Mock(username="example")
        ):
            self.app.login_easy()
        secret_prompt.assert_called_once()
        self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "new-session-secret")
        self.assertNotIn("new-session-secret", self.output.getvalue())

    def test_failed_session_login_preserves_saved_session(self):
        Path("sessionid.txt").write_text("existing-session", encoding="utf-8")
        with patch("builtins.input", side_effect=["s", "example", KeyboardInterrupt]), patch.object(
            self.app.getpass, "getpass", return_value="invalid-session-secret"
        ), patch.object(self.app.instaloader, "Instaloader"), patch.object(
            self.app.instaloader.Profile,
            "from_username",
            side_effect=self.app.instaloader.exceptions.InstaloaderException("Request failed"),
        ), self.assertRaises(KeyboardInterrupt):
            self.app.login_easy()
        self.assertEqual(Path("sessionid.txt").read_text(encoding="utf-8"), "existing-session")
        self.assertIn("Login failed", self.output.getvalue())
        self.assertNotIn("invalid-session-secret", self.output.getvalue())

    def test_main_logs_in_before_showing_menu(self):
        calls = Mock()
        with patch.object(self.app, "login_easy", calls.login), patch.object(self.app, "menu", calls.menu):
            self.app.main()
        self.assertEqual([call[0] for call in calls.mock_calls], ["login", "menu"])


if __name__ == "__main__":
    unittest.main()
