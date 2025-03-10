# 🐺 Wolvesville OGU Finder

**Wolvesville OGU Finder** is a Python script that checks username availability in **Wolvesville** using the game's API.  
It takes a list of usernames from a wordlist file and tests them dynamically, displaying only available usernames in real time.

🔹 **Fully Automated** – Checks usernames from a list (`wordlist.txt`)  
🔹 **Real-Time Console UI** – Live stats on checked, valid, and failed usernames  
🔹 **Customizable Delay** – Adjust request speed to prevent rate limiting  
🔹 **Cross-Platform** – Works on Windows, Linux, and macOS  

---

## 🚀 Features  
✔ **Checks username availability** in Wolvesville  
✔ **Uses a wordlist (`wordlist.txt`)** to test multiple usernames  
✔ **Real-time statistics**: `Checked | Valid | Failed`  
✔ **Only shows available usernames** in green  
✔ **Adjustable delay (`DELAY`)** to avoid rate-limiting  
✔ **Clean console interface** using `curses`  

---

## 📦 Installation  
### 1️⃣ Install Python  
📥 [Download Python](https://www.python.org/downloads/) and install it if you haven't already.  

### 2️⃣ Install Required Libraries  
Run this command in your terminal:  
```bash
pip install requests windows-curses
