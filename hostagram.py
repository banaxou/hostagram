# code by ovax version 1.0
# best funk [ MONTAGEM BATCHI SLOWED ]

import instaloader, fade, os
import time
import getpass
import requests
import json
from datetime import datetime


v = "v1.0"  # en blanc
q = "https://github.com/banaxou/"
white = "\033[97m"
red = "\033[91m"
BLUE = "\033[94m"
r = "\033[0m"

ban = fr"""
          code by ovax {v}  
       {fade.greenblue(q)} 

          .__                   __                                         {white}╔                ╗ {white}
          |  |__   ____  ______/  |______    ________________    _____        1: user info 
          |  |  \ /  _ \/  ___|   __\__  \  / ___\_  __ \__  \  /     \         
          |   Y  (  <_> )___ \ |  |  / __ \/ /_/  >  | \// __ \|  Y Y  \      2: id info 
          |___|  /\____/____  >|__| (____  |___  /|__|  (____  /__|_|  /
               \/           \/           \/_____/            \/      \/       3: watch user 
                                                                          {white}╚                  ╝{white}
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

def user_info():
    ig = instaloader.Instaloader()

    w = 50
    ins = input(f"> Enter Instagram username: ") or "zuck"

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
            # number phone and email 1.2 soon
            "Number of posts": user.mediacount,
            "Business category": user.business_category_name or "None",
            "Type account": 'Business' if user.is_business_account else 'Personal',
            "Private account": user.is_private,
            "Verified account": user.is_verified,
            "Has highlight reels": user.has_highlight_reels,
            "Biography hashtags": user.biography_hashtags,
            "Biography mentions": user.biography_mentions,
            "Follows viewer": user.follows_viewer,
            "Followed by viewer": user.followed_by_viewer,
            "Blocked by viewer": user.blocked_by_viewer,
            "Profile picture URL": user.profile_pic_url,
        }

        print(f"╔{'═' * w}╗")
        for key, value in info.items():
            print(f" {red} {key}{r}: {w}{value}{r}")
        input(f"╚{'═' * w}╝") 

        filex = f"{ins}.txt"  # save les data dans un fichier txt pour garder infos sur la cible 
        with open(filex, "w", encoding="utf-8") as f:
            for key, value in info.items():
                f.write(f"{key}: {value}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{red}Error{reset}: The user does not exist")




def id_info():
    session_file = "sessionid.txt"
    x= 50
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            session_id = f.read().strip()
    else:
        session_id = ""


    if not session_id:
        session_id = input("Enter your session ID : ").strip()
        with open(session_file, "w") as f:
            f.write(session_id)

    
    idx = input("enter instagram id : ").strip() or "505"

    headers = {
        "User-Agent": "Instagram 219.0.0.12.117 Android",
        "Cookie": f"sessionid={session_id}",
        "Accept": "*/*"
    }

    url = f"https://i.instagram.com/api/v1/users/{idx}/info/"
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()['user']
        print(f"╔{'═' * x}╗")
        print(f"username: {data['username']}")
        input(f"╚{'═' * x}╝")
        # plus d'info dans la 1.1
    else:
        print(f"Error {res.status_code} : {res.text}")


def truc_la(info):
    r = "\033[0m"

    try:
        width = os.get_terminal_size().columns
    except:
        width = 100

    def center(text, w=width):
        return text.center(w)

    def separator(char="─", w=None): # by IA ... elle a contribué a la creation de la focntion seperator "oui j'avais la flemme + trop complex"
        try:
            w = os.get_terminal_size().columns if w is None else w
        except:
            w = 80
        return f"{red}{char * w}{r}"

    print()
    print(separator("═"))
    print(center(" INSTAGRAM PROFILE VIEWER "))
    print(separator("═"))

    # Header
    print()
    print(center(f"{info['Full name']}  ({info['Type account']}) {'VERIFIED' if info['Verified'] == 'Yes' else ''}"))
    print(center(f"@{info['Username']}  |  ID: {info['ID']}"))
    print(center(f"[{'PRIVATE' if info['Private account'] == 'Private' else 'PUBLIC'} ACCOUNT"))
    print()

    # Followers / Followees / Posts
    print(separator("─"))
    print(center(f"Followers: {info['Followers']}   |   Following: {info['Followees']}   |   Posts: {info['Number of posts']}"))
    print(separator("─"))

    # Bio & URL
    print()
    if info['Bio']:
        print(center(f"\"{info['Bio']}\""))
    if info['Bio URL']:
        print(center(f"Link: {info['Bio URL']}"))

    print()

    # Extra Info
    print(separator("─"))
    print(center(f"Category: {info['Business category']}"))
    print(center(f"Highlights available: {info['Highlight reels']}"))
    print(separator("═"))
# end code IA

def watch_user():
    ig = instaloader.Instaloader()

    ins = input("> Enter Instagram username: ") or "zuck"
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
                "Highlight reels": "Yes" if user.has_highlight_reels else "No",
                "Profile picture URL": user.profile_pic_url,
            }

            os.system("cls" if os.name == "nt" else "clear")  
            print(f"{white}[{datetime.now()}] Profile update: {ins}{r}")
            truc_la(info)
            log_info(info)

        except instaloader.exceptions.ProfileNotExistsException:
            print(f"{red}Error : profile '{ins}' not found{r}")
            break
        except Exception as e:
            print(f"{red}Error : {e}{r}")

        time.sleep(15)  # 15s  plus chill que 5s pour eviter les ban api ou mes un vpn jsp mdrr 


def login_easy():
    os.system("cls" if os.name == "nt" else "clear")
    print(fade.greenblue(loginz))

    user_list = []
    if os.path.exists("user.txt"):
        with open("user.txt", "r") as f:
            user_list = f.read().splitlines()

    user = input("Instagram USER: ")
    session_pathx = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Instaloader\\session-{user}"
    
    try:
        os.remove(session_pathx)
    except FileNotFoundError:
        pass  # Session file doesn't exist, which is fine
    except Exception as e:
        print(f"Error deleting session file: {e}")

    if user not in user_list:
        with open("user.txt", "a") as f:
            f.write(user + "\n")

    os.system(f"instaloader --login {user}")


def menu():
    user = getpass.getuser()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(fade.pinkred(ban))
        l = input(f"      > {user}: ")
        if l.lower() == "1":
            user_info()
        elif l.lower() == "2":
            id_info()
        elif l.lower() == "3":
            watch_user()
        else:
            print("[-] Invalid choice")

def main():
    menu()

login_easy()

if __name__ == "__main__":
    main()
