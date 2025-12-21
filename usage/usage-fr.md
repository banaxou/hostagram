# 🇫🇷 Hostagram – Usage 🚀

## Conseil 💡

Avant de commencer, il est conseillé de créer un **compte Instagram dédié à l’OSINT** via votre PC

> Une version Termux est en développement

---

## Installation 🔧

### Windows

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py  # ou via go.bat
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

Après avoir exécuté Hostagram, vous serez redirigé vers une page affichant `login`.

> Connectez-vous à votre compte Instagram dédié à l’OSINT.

Vous pouvez vous connecter via :

- **Votre Session ID**
- **Votre mot de passe**

**Il est fortement conseillé d’utiliser votre Session ID**, car cela permet d’accéder à davantage d’informations sur votre cible.

---

## Menu Principal 🏠

![menu](https://github.com/banaxou/hostagram/blob/main/img/hostagram1.3.png)

Une fois connecté, vous serez redirigé vers le **menu principal**, où le logo **HOSTAGRAM** s’affiche.

> Actuellement, plusieurs fonctionnalités sont disponibles.  
D’autres seront ajoutées prochainement.

---

# Fonctionnalités ⚙️

---

## 1. `user-info` 👤

> Récupère les informations complètes d’un **profil Instagram**.

---

## 2. `id-info` 🆔

Si votre cible vous a bloqué ou a changé de pseudonyme :

1. Rendez-vous dans le dossier `hostagram`
2. Ouvrez le fichier `.json` correspondant à la cible
3. Récupérez l’**ID** du profil
4. Utilisez cet ID avec `id-info` pour retrouver son **nouveau pseudonyme**

> Fonction en cours de développement.

---

## 3. `watch-user` 👀

Compatible avec :

- Le **nom d’utilisateur**
- L’**ID** du profil

Cette fonctionnalité permet de **surveiller et enregistrer en quasi temps réel toutes les activités du profil ciblé**.

> Même si vous vous déconnectez, *Hostagram continue la surveillance*, tant que votre machine reste allumée.  
⚠️ Une utilisation excessive peut entraîner un bannissement d’IP.  
Les proxys seront ajoutés prochainement.

---

## 4. `phone-check` 📱

> Vérifie si un **numéro de téléphone** est associé à un compte Instagram.  
Indique uniquement si le numéro est lié à Instagram.

---

## 5. `email-check` 📧

> Vérifie si une **adresse email** est associée à Instagram.  
N’indique pas le nom d’utilisateur lié.

---

## 6. `username-check` 🔍

> Vérifie si un **pseudonyme** existe sur Instagram.  
N’affiche aucune autre information (abonnés, email, numéro…).

---

## 7. `follow Insight` 🔍

> Affiche la liste complète des **abonnés** d’un profil :  
> - ID  
> - Nom d’utilisateur  
> - Compte privé ou non  
> - Statut (certifié ou non)  
>
> Affiche jusqu’à **50 abonnés et abonnements** dans le terminal.  
> Toutes les données sont enregistrées dans un **fichier JSON**.

---

## 8. `List Viewer` 📄

Permet d’afficher **l’intégralité des abonnés et abonnements** d’une cible.

> **Astuce OSINT :**  
Pour rechercher une personne précise dans la liste, utilisez `grep` avec la commande correspondante.

---

## 9. `Follow Watch` ⏱️

L’une des fonctionnalités les plus puissantes d’Hostagram.

Elle permet de **surveiller en direct les activités des abonnés et abonnements** de votre cible :

- Nouvel abonnement  
- Désabonnement  
- Heure, minute et seconde exactes  
- Tout est enregistré dans un **fichier JSON**

### Exemple OSINT :

```
Une personne a disparu de votre entourage, ou quelle que soit la situation, elle ne répond plus à au messages et est supposée ne plus avoir accès à son téléphone Grâce à **Follow Watch**, Vous pourrez voir les activités des abonnements et des abonnés du compte :

- s’est abonnée à un compte
- puis  c'est désabonnée quelques minutes plus tard

Vous pouvez alors en déduire qu’elle est active sur Instagram
```

---

# À venir 🔜

Plus de **5 nouvelles fonctionnalités** sont prévues !

Hostagram est un outil OSINT Instagram **en constante évolution**

---

# ❤️ Donate

Votre soutien permet de maintenir cet outil **gratuit et open source**

### Ethereum  
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">

`0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58`

---

### Solana  
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

`BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2`

---
> **Hostagram 1.4**
