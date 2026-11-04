# Contributing

Keep pull requests focused on one problem and explain the behavior before and
after the change. For work that changes Instagram API integration, check the
existing issues first, including the version 2 discussion in
[issue #9](https://github.com/banaxou/hostagram/issues/9).

## Local setup

Create a virtual environment with `python -m venv .venv`, then activate it:

- Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
- Linux/macOS: `source .venv/bin/activate`

Install the project dependencies with `python -m pip install -r requirements.txt`.

## Tests

Run `python -m unittest discover -s tests -v` from the project root.
The login tests use temporary files and mock interactive input, subprocesses,
and Instagram calls. They require no Instagram credentials or network access
after the dependencies have been installed. They check local behavior and do
not establish compatibility with the live Instagram API.

Importing `hostagram` must not start a login prompt or change local credentials.
Run the interactive application explicitly with `python hostagram.py`.

## Local data

`sessionid.txt` and `user.txt` are created when needed and are excluded from Git,
along with generated profile exports, monitoring logs, and virtual environments.
Do not include credentials or real account data in pull requests or test fixtures.
