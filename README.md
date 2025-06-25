# 🔴 Hostagram 1.2 | The Instagram OSINT Tool

<a href="https://github.com/banaxou/hostagram/"><img src="https://img.shields.io/github/stars/banaxou/hostagram" alt="Stars Badge" /></a>
<a href="https://github.com/banaxou/hostagram/network/members"><img src="https://img.shields.io/github/forks/banaxou/hostagram" alt="Forks Badge" /></a>

![banner](https://github.com/user-attachments/assets/72532e05-2bc1-43e0-9410-a049e7716660)

**Hostagram** is a powerful OSINT tool for Instagram, designed to extract and monitor a maximum of information from any public (or accessible) Instagram account

## 🚦 Before You Start

- **Create a dedicated Instagram account for OSINT**  
  Some features require authentication
- **Hostagram never steals your password**  
- Use your own session ID for full access (public info only on private/locked accounts).

---


## 🕵️ Main Features

### 1. `user-info`  
Extracts all available info from a profile by username and saves it as `.txt` and `.json`
- Full name, username, ID
- Bio, bio URL, hashtags, mentions
- Followers, followees, number of posts
- Business category, type (personal/business) and more!

### 2. `id-info`  
Finds and displays info from a raw Instagram user ID even if the username or profile picture changed, or if you’re blocked

### 3. `watch-user`  
Monitors a profile in real time (by username or ID) and logs any changes to a file as well as to the terminal

---

## 💻 Installation

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py
```
> 🛠️ Hostagram is in active development! This is version 1.2  even more upgrades are coming

---

## 🚀 Roadmap

- v1.0: old version
- v1.1: initial release
- v1.2: **NOW!** user info : email phone 
- v1.3: soon new page + new functions
- v1.4: ??

---

## 📝 Example Output (fields extracted)

| Field                    | Value (Exemple)              |
|--------------------------|------------------------------|
| Full name                | Johnny go                    |
| Username                 | @exemple                     |
| ID                       | 123456789                    |
| Bio                      | lifestyle • Art              |
| Bio URL                  | https://exemple.com          |
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
| Profile picture URL      | https://exemple.com/photo.jpg|
| Memorialized             | False                        |
| New to Instagram         | False                        |
| WhatsApp linked          | False                        |
| HD Profile picture URL   | https://exemple.com/hd.jpg   |
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

> **Hostagram 1.2 — Ready to dominate Instagram OSINT**
---

