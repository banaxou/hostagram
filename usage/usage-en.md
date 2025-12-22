# Hostagram – Usage 🚀
# 📹 Tutorial
Watch the full tutorial here: [tuto hostagram 1.3](https://youtu.be/uQgQg_Y-20s?si=tGvP67zYI380CsTK) thx exploit buddy 

## Tip 💡

Before starting, it is recommended to create a **dedicated Instagram account for OSINT** on your PC

> A Termux version is under development

---

## Installation 🔧

### Windows 🪟

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py  # or via go.bat
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

After running Hostagram, you will be redirected to a page displaying `login`.

> Log in with your dedicated Instagram OSINT account.

You can log in using:

- **Your Session ID**
- **Your password**

**Using your Session ID is strongly recommended**, as it unlocks more detailed information about your target.

---

## Main Menu 🏠

![menu](https://github.com/banaxou/hostagram/blob/main/img/hostagram1.3.png)

Once logged in, you will be redirected to the **main menu**, where the **HOSTAGRAM** logo appears.

> Several features are currently available.  
More will be added over time.

---

# Features ⚙️

---

## 1. `user-info` 👤

> Retrieves complete information about an **Instagram profile**

---

## 2. `id-info` 🆔

If your target blocked you or changed their username:

1. Go to the `hostagram` directory  
2. Open the `.json` file corresponding to the target  
3. Retrieve the profile **ID**  
4. Use that ID with `id-info` to find their **new username**

> Feature under development

---

## 3. `watch-user` 👀

Works with:

- The **username**
- Or the **profile ID**

This feature allows you to **monitor and record all activity from the target profile**, almost in real time

> Even if you log out, *Hostagram continues monitoring*, as long as your machine stays on
⚠️ Excessive use may result in an IP ban from Instagram 
Proxy support will be added soon

---

## 4. `phone-check` 📱

> Checks whether a **phone number** is associated with an Instagram account.  
It only tells you if the number is linked — no username is revealed.

---

## 5. `email-check` 📧

> Checks whether an **email address** is associated with Instagram.  
It does not reveal the username linked to it.

---

## 6. `username-check` 🔍

> Checks whether a **username** exists on Instagram.  
Does not display additional information (followers, email, phone number…).

---

## 7. `follow Insight` 🔍

> Displays the complete list of a profile’s **followers**, including:  
> - ID  
> - Username  
> - Private or public account  
> - Verified status  
>
> Shows up to **50 followers and followings** in the terminal.  
> All data is saved into a **JSON file**.

---

## 8. `List Viewer` 📄

Displays **the full list of followers and followings** of a target.

> **OSINT Tip:**  
Use `grep` to quickly search for a specific person within the list.

---

## 9. `Follow Watch` ⏱️

One of Hostagram’s most powerful features.

It allows you to **monitor in real time the activity of a target’s followers and followings**, including:

- New follow  
- Unfollow  
- Exact timestamp (hour, minute, second)  
- Everything is saved in a **JSON file**

### OSINT Example:

```
Someone from your circle has disappeared, or for any reason is no longer responding to your messages and is supposedly unable to access their phone. Thanks to Follow Watch, you can see the activity of the account’s followers and followings:

- they followed an account,
- then unfollowed it a few minutes later

You can then deduce that the person is active on Instagram
```

---

# Coming Soon 🔜

More than **5 new features** are planned!

Hostagram is an Instagram OSINT tool that is **constantly evolving**

---

# ❤️ Donate

Your support helps keep this tool **alive and open source**

### Ethereum  
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">

`0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58`

---

### Solana  
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

`BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2`

---

> **Hostagram 1.4**
