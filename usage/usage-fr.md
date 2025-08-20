# FR Hostagram - Usage 🚀

## Conseil 💡

Avant de commencer, il est conseillé de créer un compte Instagram dédié à l’OSINT via votre PC.

> Une version Termux est en développement.

---

## Installation 🔧

### Windows 

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py # ou via go.bat
```

### Linux 🐧

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
bash linux.sh
python3 hostagram.py
```

---

## login 🔑
![login](https://github.com/banaxou/hostagram/blob/main/img/login1.3.png)

**Après avoir exécuté Hostagram, vous serez redirigé vers une page avec le texte `login`**

> Connectez-vous à votre compte Instagram dédié à l’OSINT

Vous avez le choix entre vous connecter avec votre **Session ID** ou votre **mot de passe**
**Il est conseillé d’utiliser votre Session ID** pour profiter pleinement des fonctionnalités d'Hostagram, notamment l'accès à plus d'informations sur votre cible.

---

## Menu Principal 🏠
![menu](https://github.com/banaxou/hostagram/blob/main/img/hostagram1.3.png)

**Une fois connecté, vous serez redirigé vers le menu principal où le logo __HOSTAGRAM__ s'affiche**

> Actuellement, **six fonctionnalités** sont disponibles.
D'autres options seront ajoutées avec le temps.

---

## Fonctionnalités ⚙️

### 1. `user-info` 👤

> Permet de récupérer des informations sur un **profil Instagram**

---

### 2. `id-info` 🆔

Si votre cible vous a bloqué ou a changé de pseudonyme :

* Allez dans le répertoire `hostagram`
* Ouvrez le fichier `.json` correspondant à la cible
* Récupérez l'**ID** du profil
* Utilisez cet ID avec la commande `id-info` pour retrouver son **nouveau pseudonyme**

Cette fonction est **en cours de développement**.

---

### 3. `watch-user` 👀

Cette fonctionnalité fonctionne avec :

* Le **username**
* Ou l’**ID** du profil

Cette fonction est **en cours de développement** et subira de nombreuses améliorations.

Elle permet de **surveiller et enregistrer toutes les activités du profil ciblé**, quasiment en temps réel.

> **Même si vous vous déconnectez, *Hostagram continue de traquer les moindres gestes du profil*, à condition que votre machine soit toujours en marche.
⚠️ Attention à ne pas abuser de cette fonction, car il existe un risque de bannissement d'IP par Instagram.
Les proxys ne sont pas encore présents sur Hostagram, mais ils le seront bientôt**

---

### 4. `phone-check` 📱

> **Vérifie si un numéro est associé à Instagram.
Cette fonction *vous indique seulement si le numéro est lié à Instagram*, mais ne remonte pas le nom d'utilisateur ni d'autres informations**

---

### 5. `email-check` 📧

> **Vérifie si une adresse email est associée à Instagram.
Cette fonction **vous indique seulement si l’email est lié à Instagram**, mais ne remonte pas le nom d'utilisateur ni d'autres informations**

---

### 6. `username-check` 🔍

> **Vérifie simplement si un pseudonyme est associé à Instagram. Cette fonction permet de savoir si le compte existe et est actif, mais ne remonte aucune autre information comme les abonnés, email ou numéro de téléphone**

---

## À venir 🔜

Plus de **10 nouvelles fonctionnalités** sont prévues !

Hostagram est un outil OSINT spécialisé Instagram **toujours en développement**

## ❤️ Donate

Votre soutien aide à maintenir cet outil vivant et open source !


<h1>Ethereum</h1>
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">  

[0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58](https://etherscan.io/address/0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58)

---
‎<h1>sol</h1>
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

[BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2](https://solscan.io/account/BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2)

> **Hostagram 1.3**
