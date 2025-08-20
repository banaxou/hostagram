# Hostagram - Usage 🚀

## Tip 💡

Before starting, it is recommended to create a dedicated Instagram account for OSINT on your PC.  

> A Termux version is under development.

---

## Installation 🔧

### Windows 🪟

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py # or via go.bat
```

### Linux 🐧

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
bash linux.sh
python3 hostagram.py
```

---

## Login 🔑
![login](https://github.com/banaxou/hostagram/blob/main/img/login1.3.png)

**After running Hostagram, you will be redirected to a page with the text `login`.**  

> Log in with your dedicated Instagram OSINT account.  

You can log in with either your **Session ID** or your **password**.  
**It is recommended to use your Session ID** to take full advantage of Hostagram’s features, especially access to more detailed information about your target.

---

## Main Menu 🏠
![menu](https://github.com/banaxou/hostagram/blob/main/img/hostagram1.3.png)

**Once logged in, you will be redirected to the main menu where the __HOSTAGRAM__ logo is displayed.**  

> Currently, **six features** are available.  
More options will be added over time.

---

## Features ⚙️

### 1. `user-info` 👤

> Retrieve information about an **Instagram profile**.

---

### 2. `id-info` 🆔

If your target has blocked you or changed their username:

* Go to the `hostagram` directory
* Open the `.json` file corresponding to the target
* Retrieve the profile **ID**
* Use that ID with the `id-info` command to find their **new username**

This feature is **under development**.

---

### 3. `watch-user` 👀

This feature works with:

* The **username**
* Or the profile **ID**  

This feature is **under development** and will undergo many improvements.  

It allows you to **monitor and record all the target’s profile activities**, almost in real time.  

> **Even if you log out, *Hostagram continues tracking the profile’s every action*, as long as your machine remains on.  
⚠️ Warning: do not abuse this function, as there is a risk of IP banning by Instagram.  
Proxies are not yet implemented in Hostagram, but will be added soon.**

---

### 4. `phone-check` 📱

> **Checks if a phone number is associated with Instagram.  
This feature *only indicates whether the number is linked to Instagram*, but does not reveal the username or other details.**

---

### 5. `email-check` 📧

> **Checks if an email address is associated with Instagram.  
This feature *only indicates whether the email is linked to Instagram*, but does not reveal the username or other details.**

---

### 6. `username-check` 🔍

> **Simply checks if a username is associated with Instagram.  
This feature allows you to know whether the account exists and is active, but does not provide further information such as followers, email, or phone number.**

---

## Coming Soon 🔜

More than **10 new features** are planned!  

Hostagram is an Instagram OSINT tool that is **constantly evolving**

## ❤️ Donate

Your support helps keep this tool alive and open source!

<h1>Ethereum</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">  

[0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58](https://etherscan.io/address/0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58)

---
‎<h1>sol</h1>
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

[BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2](https://solscan.io/account/BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2)

> **Hostagram 1.3**
