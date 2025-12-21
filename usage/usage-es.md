# 📖 Documentación Auxiliar  
- 👉 https://jinversor.co/2025/07/hostagram/ 1.2  
- 👉 https://esgeeks.com/hostagram-herramienta-osint/ 1.0  

# 🎥 Tutorial 1.0  
👉 https://youtu.be/ZBV1ZSwuNPw?si=xyAWMKp66J-TYC8V  

---

# Hostagram – Uso 🚀

## Consejo 💡

Antes de comenzar, se recomienda crear una **cuenta de Instagram dedicada al OSINT** desde tu PC.

> Una versión para Termux está en desarrollo.

---

## Instalación 🔧

### Windows 🪟

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py  # o mediante go.bat
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

Después de ejecutar Hostagram, serás redirigido a una página con el texto `login`

> Inicia sesión con tu cuenta de Instagram dedicada al OSINT

Puedes iniciar sesión con:

- **Tu Session ID**
- **Tu contraseña**

**Se recomienda usar tu Session ID**, ya que permite acceder a más información sobre tu objetivo

---

## Menú Principal 🏠

![menu](https://github.com/banaxou/hostagram/blob/main/img/hostagram1.3.png)

Una vez conectado, serás redirigido al **menú principal**, donde aparece el logo **HOSTAGRAM**

> Actualmente hay varias funciones disponibles
Más opciones se añadirán próximamente

---

# Funcionalidades ⚙️

---

## 1. `user-info` 👤

> Obtiene información completa de un **perfil de Instagram**

---

## 2. `id-info` 🆔

Si tu objetivo te ha bloqueado o ha cambiado su nombre de usuario:

1. Ve al directorio `hostagram`  
2. Abre el archivo `.json` correspondiente  
3. Recupera el **ID** del perfil  
4. Usa ese ID con `id-info` para encontrar su **nuevo nombre de usuario**

> Función en desarrollo.

---

## 3. `watch-user` 👀

Compatible con:

- El **nombre de usuario**
- El **ID** del perfil

Permite **supervisar y registrar en tiempo casi real todas las actividades del perfil objetivo**

> Incluso si cierras sesión, *Hostagram sigue monitoreando*, siempre que tu máquina permanezca encendida
⚠️ El uso excesivo puede provocar un baneo de IP
El soporte para proxys llegará pronto

---

## 4. `phone-check` 📱

> Verifica si un **número de teléfono** está asociado a Instagram
Solo indica si está vinculado; no revela el nombre de usuario

---

## 5. `email-check` 📧

> Verifica si un **correo electrónico** está asociado a Instagram 
No revela el nombre de usuario vinculado

---

## 6. `username-check` 🔍

> Verifica si un **nombre de usuario** existe en Instagram
No muestra información adicional (seguidores, correo, teléfono…)

---

## 7. `follow Insight` 🔍

> Muestra la lista completa de **seguidores** de un perfil, incluyendo:  
> - ID  
> - Nombre de usuario  
> - Cuenta privada o pública  
> - Estado de verificación  
>
> Muestra hasta **50 seguidores y seguidos** en la terminal
> Todos los datos se guardan en un **archivo JSON**

---

## 8. `List Viewer` 📄

Permite visualizar **la lista completa de seguidores y seguidos** de un objetivo

> **Tip OSINT:**  
Usa `grep` para buscar rápidamente un usuario dentro de la lista

---

## 9. `Follow Watch` ⏱️

Una de las funciones más potentes de Hostagram

Permite **monitorear en tiempo real la actividad de los seguidores y seguidos** del objetivo:

- Nuevos follows  
- Unfollows  
- Hora, minuto y segundo exactos  
- Todo se guarda en un **archivo JSON**

### Ejemplo OSINT:

```
Una persona de tu entorno ha desaparecido o, por cualquier motivo, ya no responde a tus mensajes y se supone que no tiene acceso a su teléfono. Gracias a Follow Watch, puedes ver la actividad de los seguidores y seguidos de la cuenta:

- se ha seguido a un perfil,
- y luego dejó de seguirlo unos minutos después

Puedes deducir que la persona está activa en Instagram
```

---

# Próximamente 🔜

Más de **5 nuevas funciones** están previstas.

Hostagram es una herramienta OSINT para Instagram **en constante evolución**

---

# ❤️ Donar

Tu apoyo ayuda a mantener esta herramienta **viva y de código abierto**

### Ethereum  
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Ethereum_logo_2014.svg" width="20">

`0x4cc818bc2C4291CEa8117D9F8D8417EE054fEA58`

---

### Solana  
<img src="https://raw.githubusercontent.com/trustwallet/assets/master/blockchains/solana/info/logo.png" width="20">

`BVMkqwkMjtTNmD5spKayhYeb6JUfmReGxGaD4kcetXp2`

---

> **Hostagram 1.4**
---

Si tu veux, je peux aussi te générer une **version ES + FR + EN alignée**, ou une **table des matières automatique** pour GitHub.
