# 📖 Documentación Auxiliar  
- 👉 https://jinversor.co/2025/07/hostagram/  1.2
- 👉 https://esgeeks.com/hostagram-herramienta-osint/  1.0

# 🎥 Tutorial 1.1  
👉 https://youtu.be/ZBV1ZSwuNPw?si=xyAWMKp66J-TYC8V  

---

# Hostagram - Uso 🚀

## Consejo 💡

Antes de comenzar, se recomienda crear una cuenta de Instagram dedicada al OSINT desde tu PC.  

> Una versión para Termux está en desarrollo.

---

## Instalación 🔧

### Windows 🪟

```bash
git clone https://github.com/banaxou/hostagram
cd hostagram
pip install -r requirements.txt
python hostagram.py # o mediante go.bat
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

**Después de ejecutar Hostagram, serás redirigido a una página con el texto `login`.**  

> Inicia sesión con tu cuenta de Instagram dedicada al OSINT.  

Puedes iniciar sesión con tu **Session ID** o con tu **contraseña**.  
**Se recomienda usar tu Session ID** para aprovechar al máximo las funciones de Hostagram, especialmente el acceso a más información sobre tu objetivo.

---

## Menú Principal 🏠
![menu](https://github.com/banaxou/hostagram/blob/main/img/hostagram1.3.png)

**Una vez conectado, serás redirigido al menú principal donde aparece el logo __HOSTAGRAM__.**  

> Actualmente, hay **seis funciones** disponibles.  
Más opciones se añadirán con el tiempo.

---

## Funcionalidades ⚙️

### 1. `user-info` 👤

> Permite obtener información sobre un **perfil de Instagram**.

---

### 2. `id-info` 🆔

Si tu objetivo te ha bloqueado o cambiado de nombre de usuario:

* Ve al directorio `hostagram`
* Abre el archivo `.json` correspondiente al objetivo
* Recupera el **ID** del perfil
* Usa ese ID con el comando `id-info` para encontrar su **nuevo nombre de usuario**

Esta función está **en desarrollo**.

---

### 3. `watch-user` 👀

Esta funcionalidad funciona con:

* El **username**
* O el **ID** del perfil  

Esta función está **en desarrollo** y sufrirá muchas mejoras.  

Permite **supervisar y registrar todas las actividades del perfil objetivo**, casi en tiempo real.  

> **Incluso si cierras sesión, *Hostagram sigue rastreando cada acción del perfil*, siempre que tu máquina permanezca encendida.  
⚠️ Atención: no abuses de esta función, ya que existe riesgo de baneo de IP por parte de Instagram.  
Los proxys aún no están presentes en Hostagram, pero se añadirán pronto.**

---

### 4. `phone-check` 📱

> **Verifica si un número está asociado a Instagram.  
Esta función *solo indica si el número está vinculado a Instagram*, pero no muestra el nombre de usuario ni otra información.**

---

### 5. `email-check` 📧

> **Verifica si una dirección de correo está asociada a Instagram.  
Esta función *solo indica si el correo está vinculado a Instagram*, pero no muestra el nombre de usuario ni otra información.**

---

### 6. `username-check` 🔍

> **Verifica si un nombre de usuario está asociado a Instagram.  
Esta función permite saber si la cuenta existe y está activa, pero no muestra otra información como seguidores, correo electrónico o número de teléfono.**

---

## Próximamente 🔜

¡Más de **10 nuevas funciones** están previstas!  

Hostagram es una herramienta OSINT especializada en Instagram **en constante desarrollo**

---

## 📚 Recursos adicionales  

- 📖 Documentación: [jinversor.co](https://jinversor.co/2025/07/hostagram/)  
- 📖 Documentación alternativa: [esgeeks.com](https://esgeeks.com/hostagram-herramienta-osint/)  
- 🎥 Tutorial 1.1: [YouTube](https://youtu.be/ZBV1ZSwuNPw?si=xyAWMKp66J-TYC8V)  
  
---
