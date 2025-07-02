# 🔴 Hostagram 1.2 | The Instagram OSINT Tool

<a href="https://github.com/banaxou/hostagram/"><img src="https://img.shields.io/github/stars/banaxou/hostagram" alt="Stars Badge" /></a>
<a href="https://github.com/banaxou/hostagram/network/members"><img src="https://img.shields.io/github/forks/banaxou/hostagram" alt="Forks Badge" /></a>

![banner](https://github.com/user-attachments/assets/72532e05-2bc1-43e0-9410-a049e7716660)

**Hostagram** is a powerful OSINT tool for Instagram, designed to extract and monitor as much information as possible from any public (or accessible) Instagram account

## 🚦 Before You Start

- **Create a dedicated Instagram account for OSINT purposes**  
  Some features require authentication
- **Hostagram never steals your password**  
- Use your own session ID for full access (only public info is available on private/locked accounts)

---

## 🕵️ Hostagram Tutorial

To begin, you need to log in with either a password or a session ID
**If you connect using your session ID, you will have more access to information**

![login-1 2V2](https://github.com/user-attachments/assets/54fc5677-df48-411d-8181-5974f6482081)


Once you are in the main menu, you have three functions: `user-info` `id-info` and `watch-user`

### 1 👤​ User Info
![image](https://github.com/user-attachments/assets/630727a4-2d44-4d60-bf8c-5fa2083a0086)  
**Enter Instagram username**  
This feature allows you to retrieve a lot of information about an Instagram profile, such as:
- Username
- Followees
- Followers
- ID
- BIO
- Public email or obfuscated email
- Obfuscated phone and more  
The data is saved in both 'json' and 'txt'

### 2 🆔​ ID Info
![image](https://github.com/user-attachments/assets/8fefea5d-e992-4ae5-a13e-d523397490d8)  
**Enter user ID**  
If you have lost access to your target's Instagram account, or if your target has changed their username or blocked you, you can always find the account using their ID
This function uses the session ID for more information on the ID
The data is saved in both 'json' and 'txt'

### 3 🔎​ Watch User
![image](https://github.com/user-attachments/assets/624a1889-d0bb-414a-a2b5-b36d2b5ffc3f)

This function allows you to receive real-time activity updates from the account: follow/unfollow, new posts, new username, and more. 
You can check if the account is active 
You can choose to monitor the profile by either user ID or username
The data is saved in both 'json' and 'txt' 

---

## 💻 Installation

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py
```

> 🛠️ Hostagram is in active development. This is version 1.2 — even more upgrades are coming!

---

## 🚀 Roadmap

- v1.0: old version
- v1.1: initial release
- v1.2: **NOW!** user info: email, phone
- v1.3: coming soon — new page + new functions
- v1.4: ??

---

## 📝 Example Output (fields extracted)

| Field                    | Value (Example)              |
|--------------------------|------------------------------|
| Full name                | Johnny go                    |
| Username                 | @example                     |
| ID                       | 123456789                    |
| Bio                      | lifestyle • Art              |
| Bio URL                  | https://example.com          |
| Followees                | 342                          |
| Followers                | 1500                         |
| Number of posts          | 56                           |
| Business category        | blog                         |
| Type account             | Business                     |
| Private account          | False                        |
| Verified account         | False                        |
| Has highlight reels      | True                         |
| Biography hashtags       | #Photography                 |
| Biography mentions       | @don_pollo @dio              |
| Follows viewer           | False                        |
| Followed by viewer       | True                         |
| Blocked by viewer        | False                        |
| Profile picture URL      | https://example.com/photo.jpg|
| Memorialized             | False                        |
| New to Instagram         | False                        |
| WhatsApp linked          | False                        |
| HD Profile picture URL   | https://example.com/hd.jpg   |
| Public email             | contact@****.com             |
| Obfuscated email         | co****@m**s.com              |
| Obfuscated phone         | +** * ** ** ** 25            |
| Lookup message           | "Success"                    |

---

## 🌸 Contribute

**Issues and PRs are welcome!**  
Want to suggest an improvement or help with code? Open an issue or pull request!

---

## ❤️ Donate

Your support helps keep this tool alive and open source!

<h1>Ethereum</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">  

[0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58](https://etherscan.io/address/0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58)

---
‎<h1>sol</h1>
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

[BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2](https://solscan.io/account/BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2)

> **Hostagram 1.2**
---

