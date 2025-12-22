# code by ovax version 1.4
# best funk [ REZA TORTA | MTG batchi ]

import instaloader, fade, os
import time
import getpass
import pycountry
import json
import hmac
import hashlib
import urllib.parse
import httpx
import asyncio
import base64
import requests
from datetime import datetime
from urllib.parse import quote_plus
from json import dumps, decoder
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code

apix = 'https://i.instagram.com/api/v1/users/lookup/'
sig_key = '4'
KEY = 'e6358aeede676184b9fe702b30f4fd35e71744605e39d2181a34cede076b3c33'
v = "v1.4"
q = "https://github.com/banaxou/"
white = "\033[97m"
b = "\033[94m"
g = "\033[92m"
r = "\033[0m"
R = "\033[91m"

RED = "\033[91m"
GRN = "\033[92m"
BLU = "\033[94m"
YEL = "\033[93m"
CYN = "\033[96m"
BOLD = "\033[1m"
RST = "\033[0m"
MAG = "\033[95m"

bann = """
          .__                   __                                         
          |  |__   ____  ______/  |______    ________________    _____        
          |  |  \ /  _ \/  ___|   __\__  \  / ___\_  __ \__  \  /     \         
          |   Y  (  <_> )___ \ |  |  / __ \/ /_/  >  | \// __ \|  Y Y  \      
          |___|  /\____/____  >|__| (____  |___  /|__|  (____  /__|_|  /
               \/           \/           \/_____/            \/      \/
"""
ban  = fr"""
          code by ovax {v}  
       {fade.greenblue(q)} 
          .__                   __                                         ╭─────────────────────╮
          |  |__   ____  ______/  |______    ________________    _____     │   [1] user info     │
          |  |  \ /  _ \/  ___|   __\__  \  / ___\_  __ \__  \  /     \    │                     │
          |   Y  (  <_> )___ \ |  |  / __ \/ /_/  >  | \// __ \|  Y Y  \   │   [2] id info       │
          |___|  /\____/____  >|__| (____  |___  /|__|  (____  /__|_|  /   │                     │
               \/           \/           \/_____/            \/      \/    │   [3] watch user    │
                                                                           ╰─────────────────────╯
                                                                                                    {R}>{r} 4 new page
"""
ban2 = fr"""code by ovax  {v}
{fade.greenblue(q)}

     {bann}
        ╭───────────────────[ hostagram {v} ]──────────────────╮
        │                                                       │
        │ • [5] Phone Number     • [8] Follow Insight           │
        │                                                       │
        │ • [6] Email            • [9] List Viewer              │
        │                                                       │
        │ • [7] User Check       • [10] Follow Watch            │
        ╰───────────────────────────────────────────────────────╯

{R}<{r} 0 menu
"""


loginz = fr"""

               .__                .__        
               |  |   ____   ____ |__| ____  
               |  |  /  _ \ / ___\|  |/    \ 
               |  |_(  <_> / /_/  |  |   |  \
               |____/\____/\___  /|__|___|  /
                          /_____/         \/ 

          version {v}     === LOGIN INSTAGRAM ===  
          code by ovax 
"""

async def datax(query):
    def generate_sig(data):
        return 'ig_sig_key_version=' + sig_key + '&signed_body=' + hmac.new(
            KEY.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha256
        ).hexdigest() + '.' + urllib.parse.quote_plus(data)

    def cook_data(q):
        return {
            'login_attempt_count': '0',
            'directly_sign_in': 'true',
            'source': 'default',
            'q': q,
            'ig_sig_key_version': sig_key
        }

    async with httpx.AsyncClient(timeout=15.0) as client:
        data = generate_sig(json.dumps(cook_data(query)))
        headers = {
            "Accept-Language": "en-US",
            "User-Agent": "Instagram 101.0.0.15.120",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
            "X-FB-HTTP-Engine": "Liger",
            "Connection": "close"
        }
        try:
            r = await client.post(apix, headers=headers, data=data)
            rep = r.json()
            if "message" in rep and rep["message"] == "No users found":
                return False
            else:
                return True
        except Exception as e:
            print(f"[{R}!{r}] {R}Error during verification {r}: {e}")
            return False

def datax_user():
    p = input(f"{R}>{r} Enter username:  ").strip()
    if not p:
        print(f"{R}Empty username{r}")
        time.sleep(1)
        return
    try:
        exists = asyncio.run(datax(p))
        if exists:
            input(f"[{g}+{r}] {p} is associated with Instagram")
        else:
            print(f"[{R}-{r}] {p} is not associated with any Instagram account")
            time.sleep(2)
    except Exception as ex:
        print(f"[{R}!{r}] Error: {ex}")
        time.sleep(2)

def datax_email():
    e = input(f"{R}>{r} Enter email: ").strip().replace(" ", "")
    if not e:
        print(f"{R}Empty email{r}")
        time.sleep(1)
        return
    try:
        exists = asyncio.run(datax(e))
        if exists:
            input(f"[{g}+{r}] True {e} is associated with Instagram")
        else:
            print(f"[{R}-{r}] {e} is not associated with any Instagram account")
            time.sleep(2)
    except Exception as ex:
        print(f"[{R}!{r}] {R} Error {r}: {ex}")
    time.sleep(1)

def datax_phone():
    p = input(f"{R}>{r} Enter phone number (with country code +xx xxxxxxxxxx): ").strip()
    if not p:
        print(f"{R}Empty phone number{r}")
        time.sleep(1)
        return
    try:
        exists = asyncio.run(datax(p))
        if exists:
            input(f"[{g}+{r}] {p} is associated with Instagram")
        else:
            print(f"[{R}-{r}] {p} is not associated with any Instagram account")
            time.sleep(2)
    except Exception as ex:
        print(f"[{R}!{r}] Error: {ex}")
        time.sleep(2)
    input("")

def show_list():
    files = [f for f in os.listdir('.') if f.endswith('.json')]
    if not files:
        print(f"{R}No JSON files found{r}")
        return
    os.system("cls" if os.name == "nt" else "clear")
    print(f"┌──────────────[{R} Available JSON files {r}]──────────────┐")
    for f in files:
        print(f" {R}-{r} {f}")
    print("└──────────────────────────────────────────────────────────┘")

    filename = input(f"{R}>{r} Enter the JSON file name: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    if filename not in files:
        print(f"{R}File not found{r}")
        time.sleep(2)
        return

    try:
        with open(filename, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"{R}Error loading the JSON:{r} {e}")
        time.sleep(2)
        return

    def print_user(username="N/A", full="N/A", uid="N/A", private="N/A", verified="N/A"):
        print(f"{R}Username{r}: {username}")
        print(f"{R}Full Name{r}: {full}")
        print(f"{R}ID{r}: {uid}")
        print(f"{R}Private{r}: {private}")
        print(f"{R}Verified{r}: {verified}")
        print("──────────────────────────")

    if isinstance(data, list):
        for u in data:
            if isinstance(u, dict):
                print_user(
                    username=u.get("username"),
                    full=u.get("full_name") or u.get("name"),
                    uid=u.get("id") or u.get("pk"),
                    private=u.get("is_private"),
                    verified=u.get("is_verified"),
                )
    elif isinstance(data, dict) and "users" in data:
        for u in data["users"]:
            print_user(
                username=u.get("username"),
                full=u.get("full_name"),
                uid=u.get("pk"),
                private=u.get("is_private"),
                verified=u.get("is_verified"),
            )
    else:
        print(json.dumps(data, indent=4, ensure_ascii=False))

    input("")

def datax_follow(sessionId):
    headers = {
        "User-Agent": "Instagram 123.0.0.21.114",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-IG-App-ID": "936619743392459",
    }

    print("")
    usid = input(f"{R}>{r} Enter Instagram username: ")

    resp = requests.get(
        f"https://i.instagram.com/api/v1/users/web_profile_info/?username={usid}",
        headers=headers,
        cookies={'sessionid': sessionId}
    )
    if resp.status_code == 404:
        print(f"{R}User doesn't exist{r}")
        time.sleep(2)
        return

    if resp.status_code != 200:
        print(f"Instagram error: {resp.status_code}")
        time.sleep(2)
        return

    try:
        user_id = resp.json()["data"]["user"]["id"]
    except:
        print(f"{R}Unable to extract data error{r}")
        time.sleep(2)
        return

    def follow_h(user_id, rel_type="followers"):
        all_users = []
        next_max_id = ""
        while True:
            url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{rel_type}/"
            if next_max_id:
                url += f"?max_id={next_max_id}"
            r = requests.get(url, headers=headers, cookies={'sessionid': sessionId})
            if r.status_code == 404:
                print(f"{R}Private account{r}")
                time.sleep(2)
                return []
            if r.status_code != 200:
                print(f"{R}API error: {r.status_code}{r}")
                time.sleep(1)
                break
            try:
                data = r.json()
            except:
                print(f"{R}json error{r}")
                time.sleep(1)
                break
            for u in data.get("users", []):
                all_users.append({
                    "id": u.get("pk"),
                    "username": u.get("username"),
                    "full_name": u.get("full_name"),
                    "is_verified": u.get("is_verified"),
                    "is_private": u.get("is_private"),
                })
            next_max_id = data.get("next_max_id")
            if not next_max_id:
                break
        return all_users

    followers = follow_h(user_id, "followers")
    followings = follow_h(user_id, "following")

    if not followers and not followings:
        print(f"{R}Private account{r}")
        time.sleep(2)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n┌─────────[ {R}FOLLOWERS{r} ]──────────────────────[ {R}FOLLOWING{r} ]───────────────────────┐\n")
        max_50 = 50
        max_view = min(max_50, max(len(followers), len(followings)))
        for i in range(max_view):
            left = ""
            right = ""
            if i < len(followers):
                f_user = followers[i]
                left = (
                    f"{R}Username{r} : {f_user['username']}\n"
                    f"{R}Full name{r} : {f_user['full_name']}\n"
                    f"{R}ID{r} : {f_user['id']}\n"
                    f"{R}Verified{r} : {f_user['is_verified']}\n"
                    f"{R}Private {r}: {f_user['is_private']}"
                )
            if i < len(followings):
                fo_user = followings[i]
                right = (
                    f"{R}Username{r}: {fo_user['username']}\n"
                    f"{R}Full name{r}: {fo_user['full_name']}\n"
                    f"{R}ID {r}: {fo_user['id']}\n"
                    f"{R}Verified {r}: {fo_user['is_verified']}\n"
                    f"{R}Private {r}: {fo_user['is_private']}"
                )
            left_line = left.split("\n") if left else []
            right_line = right.split("\n") if right else []
            for j in range(max(len(left_line), len(right_line))):
                l = left_line[j] if j < len(left_line) else ""
                ri = right_line[j] if j < len(right_line) else ""
                print(f"  {l:<45}     {ri:<45}")
            print()

        with open(f"{usid}_followers.json", "w", encoding="utf-8") as f:
            json.dump(followers, f, ensure_ascii=False, indent=4)
        with open(f"{usid}_following.json", "w", encoding="utf-8") as f:
            json.dump(followings, f, ensure_ascii=False, indent=4)

        print("└───────────────────────────────────────────────────────────────────────────────┘")
        input("")
        print(f"{BLU} Followings | followers Data has been saved to {usid}_following.json | {usid}_followers.json{r} ")
        time.sleep(2)

def banner(username):
    os.system("cls" if os.name == "nt" else "clear")
    width = 44
    header = "FOLLOWER / FOLLOWING TRACKER"

    print(f"{RED}╭{'─' * width}╮{RST}")
    print(f"{RED}│{RST} {CYN}{header.center(width - 1)}{RST}{RED}│{RST}")
    print(f"{RED}│{RST} {YEL}{username.center(width - 1)}{RST}{RED}│{RST}")
    print(f"{RED}╰{'─' * width}╯{RST}\n")

def fetch_all(sessionId, user_id, rel_type, headers):
    users = set()
    next_max_id = ""

    while True:
        url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{rel_type}/"
        if next_max_id:
            url += f"?max_id={next_max_id}"

        r = requests.get(url, headers=headers, cookies={'sessionid': sessionId})
        if r.status_code != 200:
            break

        try:
            data = r.json()
        except:
            break

        for u in data.get("users", []):
            users.add(u.get("username"))

        next_max_id = data.get("next_max_id")
        if not next_max_id:
            break

    return users

def follow_watch(sessionId):
    headers = {
        "User-Agent": "Instagram 123.0.0.21.114",
        "X-IG-App-ID": "936619743392459"
    }

    username = input(f"{R}>{r} Enter Instagram username: ").strip()
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"

    resp = requests.get(url, headers=headers, cookies={'sessionid': sessionId})
    if resp.status_code != 200:
        print(f"{R}API error: {resp.status_code}{RST}")
        return

    try:
        user = resp.json()["data"]["user"]
    except:
        print(f"{R}Invalid response{RST}")
        return

    user_id = user["id"]
    followers_count = user["edge_followed_by"]["count"]
    following_count = user["edge_follow"]["count"]

    followers = fetch_all(sessionId, user_id, "followers", headers)
    followings = fetch_all(sessionId, user_id, "following", headers)
    old_counts = (followers_count, following_count)

    print(f"{YEL}Initial snapshot loaded: {followers_count} followers, {following_count} following{RST}")
    time.sleep(2)

    history = []
    width = 44

    try:
        while True:
            banner(username)

            resp = requests.get(url, headers=headers, cookies={'sessionid': sessionId})
            if resp.status_code != 200:
                time.sleep(10)
                continue

            data = resp.json()["data"]["user"]

            followers_count = data["edge_followed_by"]["count"]
            following_count = data["edge_follow"]["count"]

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            delta_f = followers_count - old_counts[0]
            delta_fg = following_count - old_counts[1]
            followers_t = f"Followers : {GRN}{followers_count}{RST} ({YEL}{'+' if delta_f > 0 else ''}{delta_f}{RST})"
            following_t = f"Following : {GRN}{following_count}{RST} ({YEL}{'+' if delta_fg > 0 else ''}{delta_fg}{RST})"
            
            print(f"{RED}╭{'─' * width}╮{RST}")
            print(f"{RED}│                                            │{RST}")
            print(f"{RED}│{RST}{YEL}{username:^{width}}{RST}{RED}│{RST}")
            print(f"{RED}│{RST}{now:^{width}}{RED}│{RST}")
            print(f"{RED}├{'─' * width}┤{RST}")
            print(f"{RED}│{RST}{followers_t:^{width}}                  {RED}│{RST}")
            print(f"{RED}│{RST}{following_t:^{width}}                  {RED}│{RST}")
            print(f"{RED}╰{'─' * width}╯{RST}")


            if delta_f != 0:
                new_followers = fetch_all(sessionId, user_id, "followers", headers)
                if delta_f > 0:
                    for u in new_followers - followers:
                        print(f"{GRN}[{now}] + {u} followed {username}{RST}")
                        history.append({"time": now, "action": "followed", "user": u})
                else:
                    for u in followers - new_followers:
                        print(f"{RED}[{now}] - {u} unfollowed {username}{RST}")
                        history.append({"time": now, "action": "unfollowed", "user": u})
                followers = new_followers

            if delta_fg != 0:
                new_following = fetch_all(sessionId, user_id, "following", headers)
                if delta_fg > 0:
                    for u in new_following - followings:
                        print(f"{RED}[{now}] + {username} now follows {u}{RST}")
                        history.append({"time": now, "action": "target_followed", "user": u})
                else:
                    for u in followings - new_following:
                        print(f"{RED}[{now}] - {username} no longer follows {u}{RST}")
                        history.append({"time": now, "action": "target_unfollowed", "user": u})
                followings = new_following

            old_counts = (followers_count, following_count)

            with open(f"{username}_changes.json", "w", encoding="utf-8") as f:
                json.dump(history, f, ensure_ascii=False, indent=4)

            time.sleep(10)

    except KeyboardInterrupt:
        print(f"{RED}Stopped by user{RST}")
        
def menu_2():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        u = getpass.getuser()
        print(fade.purplepink(ban2))
        w = input(f"{R}>{r} {u}: ").strip()

        if w == "5":
            datax_phone()
        elif w == "6":
            datax_email()
        elif w == "7":
            datax_user()
        elif w == "8":
            session_file = "sessionid.txt"

            if not os.path.exists(session_file):
                print(f"{R}No session id found,log in with  session id {r}")
                time.sleep(2)
                continue

            with open(session_file, "r") as f:
                sessionId = f.read().strip()

            if not sessionId:
                print(f"{R}No session id found,log in with  session id {r}")
                time.sleep(2)
                continue

            datax_follow(sessionId)
        elif w == "9":
            show_list()
        elif w == "10":
            session_file = "sessionid.txt"

            if not os.path.exists(session_file):
                print(f"{R}No session id found,log in with  session id {r}")
                time.sleep(2)
                continue

            with open(session_file, "r") as f:
                sessionId = f.read().strip()

            if not sessionId:
                print(f"{R}No session id found,log in with  session id {r}")
                time.sleep(2)
                continue

            follow_watch(sessionId)
        elif w == "0":
            return
        else:
            print(f"[{R}-{r}] Invalid choice")
            time.sleep(1)

def getUserId(username, sessionId):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "x-ig-app-id": "936619743392459"
    }
    api = requests.get(
        f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}',
        headers=headers,
        cookies={'sessionid': sessionId}
    )
    try:
        if api.status_code == 404:
            return {"id": None, "error": "User not found"}
        user_id = api.json()["data"]['user']['id']
        return {"id": user_id, "error": None}
    except decoder.JSONDecodeError:
        return {"id": None, "error": "Rate limit or bad session"}

def getInfo(search, sessionId, searchType="username"):
    if searchType == "username":
        data = getUserId(search, sessionId)
        if data["error"]:
            return data
        userId = data["id"]
    else:
        try:
            userId = str(int(search))
        except ValueError:
            return {"user": None, "error": "Invalid ID"}

    try:
        response = requests.get(
            f'https://i.instagram.com/api/v1/users/{userId}/info/',
            headers={'User-Agent': 'Instagram 292.0.0.17.111 Android (29/10; 420dpi; 1080x2340; generic; generic; generic; en_US)'},
            cookies={'sessionid': sessionId}
        )
        if response.status_code == 429:
            return {"user": None, "error": "Rate limit"}
        response.raise_for_status()
        info_user = response.json().get("user")
        if not info_user:
            return {"user": None, "error": "Not found"}
        info_user["userID"] = userId
        return {"user": info_user, "error": None}
    except requests.exceptions.RequestException:
        return {"user": None, "error": "Request error or bad session"}

def lookup(username):
    data = "signed_body=SIGNATURE." + quote_plus(dumps(
        {"q": username, "skip_recovery": "1"},
        separators=(",", ":")
    ))
    api = requests.post(
        'https://i.instagram.com/api/v1/users/lookup/',
        headers={
            "Accept-Language": "en",
            "User-Agent": "Instagram 292.0.0.17.111 Android (29/10; 420dpi; 1080x2340; generic; generic; generic; en_US)",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-IG-App-ID": "124024574287414",
            "Content-Length": str(len(data))
        },
        data=data
    )

    try:
        return {"user": api.json(), "error": None}
    except decoder.JSONDecodeError:
        return {"user": None, "error": "rate limit"}

def user_info():
    ig = instaloader.Instaloader()
    bb = "\033[1;34m"

    session_file = "sessionid.txt"
    session_id = ""
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            session_id = f.read().strip()

    ins = input(f"{R}>{r} Enter Instagram username: ") or "zuck"
    os.system("cls" if os.name == "nt" else "clear")
    try:
        ig.context._session.cookies.set("sessionid", session_id)

        user = instaloader.Profile.from_username(ig.context, ins)
        result_info = getInfo(ins, session_id)
        lookup_info = lookup(ins)

        info = {
            "Full name": user.full_name,
            "Username": user.username,
            "ID": user.userid,
            "Bio": user.biography,
            "Bio URL": user.external_url,
            "Followees": user.followees,
            "Followers": user.followers,
            "Number of posts": user.mediacount,
            "Business category": user.business_category_name or "None",
            "Type account": 'Business' if user.is_business_account else 'Personal',
            "Private account": user.is_private,
            "Verified account": user.is_verified,
            "Has highlight reels": user.has_highlight_reels,
            "Biography hashtags": [str(tag) for tag in user.biography_hashtags],
            "Biography mentions": [str(mention) for mention in user.biography_mentions],
            "Follows viewer": user.follows_viewer,
            "Followed by viewer": user.followed_by_viewer,
            "Blocked by viewer": user.blocked_by_viewer,
            "Profile picture URL": user.profile_pic_url
        }

        if result_info["user"]:
            u = result_info["user"]
            info.update({
                "Memorialized": u.get("is_memorialized"),
                "New to Instagram": u.get("is_new_to_instagram"),
                "WhatsApp linked": u.get("is_whatsapp_linked"),
                "HD Profile picture URL": u.get("hd_profile_pic_url_info", {}).get("url"),
                "Public email": u.get("public_email"),
            })
            if u.get("public_phone_number"):
                phone = f"+{u.get('public_phone_country_code', '')}{u.get('public_phone_number')}"
                try:
                    pn = phonenumbers.parse(phone)
                    cc = region_code_for_country_code(pn.country_code)
                    country = pycountry.countries.get(alpha_2=cc)
                    phone += f" ({country.name})"
                except:
                    pass
                info["Public phone"] = phone

        if lookup_info["user"]:
            u = lookup_info["user"]
            info.update({
                "Obfuscated email": u.get("obfuscated_email"),
                "Obfuscated phone": u.get("obfuscated_phone"),
                "Lookup message": u.get("message")
            })

        title = f"[ {R}User info{r} ]"
        line = "─" * (45 - len(title)//2)
        print("")
        print(f"┌{line}{title}{line}┐")
        print("")
        for key, value in info.items():
            print(f" {R}{key}{r}: {value}")
        print("")
        input(f"└{'─' * (len(line)*2 + len(title))}┘")

        file_txt = f"{ins}.txt"
        with open(file_txt, "w", encoding="utf-8") as f_txt:
            for key, value in info.items():
                f_txt.write(f"{key}: {value}\n")

        xjson = f"{ins}.json"
        with open(xjson, "w", encoding="utf-8") as jsson:
            json.dump(info, jsson, ensure_ascii=False, indent=4)
        print("")
        print(f"{bb}Data has been saved to {file_txt} and {xjson}{r}")
        time.sleep(2)

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{R}Error{r}: The user does not exist")
        time.sleep(1)
    except Exception as e:
        print(f"{R}Unexpected error{r}: {e}")

def id_info():
    s = instaloader.Instaloader()
    bb = "\033[1;34m"

    user_id = input(f"{R}>{r} Enter Instagram ID: ") or "176702683"

    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    headers = {
        "User-Agent": "Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; en_US)",
    }

    try:
        res = requests.get(url, headers=headers)

        if res.status_code == 200:
            data = res.json()
            username = data.get("user", {}).get("username")

            if username:
                try:
                    profile = instaloader.Profile.from_username(s.context, username)

                    info = {
                        "ID": user_id,
                        "Username": profile.username,
                        "Full name": profile.full_name,
                        "Bio": profile.biography,
                        "Followers": profile.followers,
                        "Followees": profile.followees,
                        "Number of posts": profile.mediacount,
                        "Private account": profile.is_private,
                        "Verified account": profile.is_verified,
                        "Profile picture URL": profile.profile_pic_url,
                    }
                    os.system("cls" if os.name == "nt" else "clear")
                    title = f"[ {R}ID info{r} ]"
                    line = "─" * (45 - len(title)//2)
                    print("")
                    print(f"┌{line}{title}{line}┐")
                    print("")
                    for key, value in info.items():
                        print(f" {R}{key}{r}: {value}")
                    print("")
                    input(f"└{'─' * (len(line)*2 + len(title))}┘")

                    file_txt = f"{username}_id.txt"
                    with open(file_txt, "w", encoding="utf-8") as f_txt:
                        for key, value in info.items():
                            f_txt.write(f"{key}: {value}\n")

                    xjson = f"{username}_id.json"
                    with open(xjson, "w", encoding="utf-8") as jsson:
                        json.dump(info, jsson, ensure_ascii=False, indent=4)

                    print("")
                    print(f"{bb}Data has been saved to {file_txt} and {xjson}{r}")
                    time.sleep(2)

                except Exception as e:
                    print(f"{R}Instaloader error{r}: {e}")
            else:
                print(f"{R}Error{r}: Username not found")

    except Exception as e:
        print(f"{R}Unexpected error{r}: {e}")

def decox(info):
    bold = "\033[1m"
    gray = "\033[90m"
    blue = "\033[94m"
    yellow = "\033[93m"
    white = "\033[97m"

    try:
        width = os.get_terminal_size().columns
    except:
        width = 100

    def center(text, w=width):
        return text.center(w)

    def separator(char="─", w=None, color=white):
        try:
            w = os.get_terminal_size().columns if w is None else w
        except:
            w = 80
        return color + char * w + r

    os.system("cls" if os.name == "nt" else "clear")

    title = "INSTAGRAM PROFILE"
    print(separator("═", color=blue))
    print(center(bold + white + title + r))
    print(separator("═", color=blue))
    time.sleep(0.2)

    full_name = info.get('Full name', 'N/A')
    account_type = info.get('Type account', 'N/A')
    verified = f"{blue}✔ VERIFIED{r}" if info.get('Verified account', 'No') == 'Yes' or info.get('Verified', 'No') == 'Yes' else ""
    print(center(f"{bold}{full_name}{r} {gray}({account_type}){r} {verified}"))
    time.sleep(0.1)

    print(center(f"{yellow}@{info.get('Username', 'N/A')}{r}  {gray}|{r}  ID: {info.get('ID', 'N/A')}"))
    time.sleep(0.1)

    privacy = f"{yellow}PRIVATE ACCOUNT{r}" if info.get('Private account', False) else f"{blue}PUBLIC ACCOUNT{r}"
    print(center(f"[{privacy}]"))
    time.sleep(0.1) # bug don't fixe don't touch

    print(separator("─", color=gray))

    followers = info.get('Followers', 'N/A')
    followees = info.get('Followees', 'N/A')
    posts = info.get('Number of posts', 'N/A')
    stats_line = f"{white}Followers: {yellow}{followers}{r}   {gray}|{r}   {white}Following: {yellow}{followees}{r}   {gray}|{r}   {white}Posts: {yellow}{posts}{r}"
    print(center(stats_line))
    time.sleep(0.1)

    print(separator("─", color=gray))

    if info.get('Bio'):
        print()
        print(center(f"{gray}\"{white}{info['Bio']}{gray}\"{r}"))
        time.sleep(0.1)
    if info.get('Bio URL'):
        print(center(f"{blue}{info['Bio URL']}{r}"))
        print()
        time.sleep(0.1)

    print(separator("─", color=gray))
    print(center(f"{white}Category: {yellow}{info.get('Business category', 'N/A')}{r}"))
    print(center(f"{white}Highlights available: {yellow}{info.get('Has highlight reels', info.get('Highlight reels', 'N/A'))}{r}"))
    print(separator("═", color=blue))


def watch_id():
    ig = instaloader.Instaloader()
    idx = input(f"{R}>{r} Enter Instagram ID: ") or "314216"
    log_file = f"{idx}_log.txt"

    def log_info(info_dict):
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n=== {datetime.now()} ===\n")
            for key, value in info_dict.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")

    url = f"https://i.instagram.com/api/v1/users/{idx}/info/"
    headers = {
        "User-Agent": "Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; en_US)",
    }

    while True:
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                username = data.get("user", {}).get("username")
                if not username:
                    print(f"{R}Error: Username not found for ID '{idx}'{r}")
                    time.sleep(2)
                    break
            else:
                print(f"{R}Error: {res.status_code}{r}")
                time.sleep(2)
                break

            try:
                profile = instaloader.Profile.from_username(ig.context, username)
                info = {
                    "ID": idx,
                    "Username": profile.username,
                    "Full name": profile.full_name,
                    "Bio": profile.biography,
                    "Bio URL": profile.external_url,
                    "Followees": profile.followees,
                    "Followers": profile.followers,
                    "Number of posts": profile.mediacount,
                    "Business category": profile.business_category_name or "None",
                    "Type account": 'Business' if profile.is_business_account else 'Personal',
                    "Private account": "Private" if profile.is_private else "Public",
                    "Verified": "Yes" if profile.is_verified else "No",
                    "Has highlight reels": "Yes" if profile.has_highlight_reels else "No",
                    "Profile picture URL": profile.profile_pic_url,
                }

                os.system("cls" if os.name == "nt" else "clear")
                print(f"{white}[{datetime.now()}] Profile update for ID {idx}: {username}{r}")
                decox(info)
                log_info(info)

            except instaloader.exceptions.ProfileNotExistsException:
                print(f"{R}Error: Profile with username '{username}' not found{r}")
                time.sleep(2)
                break
            except instaloader.exceptions.ConnectionException as e:
                print(f"{R}Connection error: {e}{r}")
                time.sleep(2)
                break
            except Exception as e:
                print(f"{R}Unexpected error: {e}{r}")
                time.sleep(2)
                break

        except requests.exceptions.RequestException as e:
            print(f"{R}Request error: {e}{r}")
            time.sleep(2)
            break
        except Exception as e:
            print(f"{R}Unexpected error: {e}{r}")
            time.sleep(2)
            break

        try:
            time.sleep(10)
        except KeyboardInterrupt:
            print(f"{R}Stopped by user{r}")
            break

def watch_user():
    ig = instaloader.Instaloader()

    ins = input(f"{R}>{r} Enter Instagram username: ") or "zuck"
    log_file = f"{ins}_log.txt"

    def log_info(info_dict):
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n=== {datetime.now()} ===\n")
            for key, value in info_dict.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")

    while True:
        try:
            user = instaloader.Profile.from_username(ig.context, ins)

            info = {
                "Full name": user.full_name,
                "Username": user.username,
                "ID": user.userid,
                "Bio": user.biography,
                "Bio URL": user.external_url,
                "Followees": user.followees,
                "Followers": user.followers,
                "Number of posts": user.mediacount,
                "Business category": user.business_category_name or "None",
                "Type account": 'Business' if user.is_business_account else 'Personal',
                "Private account": "Private" if user.is_private else "Public",
                "Verified": "Yes" if user.is_verified else "No",
                "Has highlight reels": "Yes" if user.has_highlight_reels else "No",
                "Profile picture URL": user.profile_pic_url,
            }

            os.system("cls" if os.name == "nt" else "clear")
            print(f"{white}[{datetime.now()}] Profile update: {ins}{r}")
            decox(info)
            log_info(info)

        except instaloader.exceptions.ProfileNotExistsException:
            print(f"{R}Error: profile '{ins}' not found{r}")
            time.sleep(2)
            break
        except Exception as e:
            print(f"{R}Error: {e}{r}")
            time.sleep(2)

        try:
            time.sleep(20)
        except KeyboardInterrupt:
            print(f"{R}Stopped by user{r}")
            break

def watch_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(fade.pinkred(bann))
        print("Do you want to watch a user by:")
        print()
        print(f"[{R}i{r}] - Instagram ID")
        print(f"[{R}u{r}] - Instagram Username")
        print(f'[{R}m{r}] - Menu')

        choice = input(f"{b}>{r} Enter your choice (i|u|m): ").strip().lower()

        if choice == 'i':
            watch_id()
        elif choice == 'u':
            watch_user()
        elif choice == 'm':
            return
        else:
            print(f"{R}Invalid choice Please select either (i/u/m){r}")
            time.sleep(2)

def login_easy():
    os.system("cls" if os.name == "nt" else "clear")
    
    user_list = []
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as f:
            user_list = f.read().splitlines()

    while True:
        open("sessionid.txt", "w").close()
        os.system("cls" if os.name == "nt" else "clear")
        print(fade.greenblue(loginz))
        print(f"{R}If you connect with the session ID, you will have more access to the information{r} ")
        m = input(f"{b}>{r} Do you want to login with password or session ID (p|s): ").lower().strip()
        
        if m == "p":
            user = input(f"{R}>{r} Instagram USERNAME: ").strip()
            session_pathx = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Instaloader\\session-{user}"
            session_linuxien = f"/home/{getpass.getuser()}/.config/instaloader/session-{user}"
            
            try:
                os.remove(session_pathx)
                os.remove(session_linuxien)
            except FileNotFoundError:
                pass
            
            if user not in user_list:
                with open("user.txt", "a") as f:
                    f.write(user + "\n")
            
            os.system(f"instaloader --login {user}")
            break

        elif m == "s":
            ig = instaloader.Instaloader()
            uzer = input(f"{R}>{r} Enter username: ").strip()
            session = input(f"{R}>{r} Enter session ID: ").strip()
            ig.context._session.cookies.set("sessionid", session)
            profile = instaloader.Profile.from_username(ig.context, uzer)
            print(f"Successfully logged in as: {profile.username}")
            time.sleep(1)
            
            with open("sessionid.txt", "w") as f:
                f.write(session)
                break
        else:
            print(f"[{R}-{r}] Invalid choice. Please enter 'p' or 's'")
            time.sleep(1)

def menu():
    user = getpass.getuser()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(fade.pinkred(ban))
        l = input(f"      {R}>{r} {user}: ")
        if l.lower() == "1":
            user_info()
        elif l.lower() == "2":
            id_info()
        elif l.lower() == "3":
            watch_menu()
        elif l.lower() == "4":
            menu_2()
        else:
            print(f"[{R}-{r}] {R}Invalid choice{r}")

def main():
    menu()

login_easy()

if __name__ == "__main__":
    main()
