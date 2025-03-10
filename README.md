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
pip install requests windows-curses

## 🔑 How to Get Your Bearer Token
To check usernames, you must authenticate with a Bearer Token from Wolvesville.

## 📜 Steps to Get Your Bearer Token
Open Wolvesville on your phone or PC
Log in to your account
Open Developer Tools (Press F12 on PC or use a tool like Charles Proxy on mobile)
Find a request sent to the API
Open Network tab
Look for a request to https://core.api-wolvesville.com/players/self
Look for the Authorization header
Copy the Bearer Token (It looks like: eyJhbGciOiJSUzI1Ni...)
Paste the token into the script
Open script.py and replace this line:
TOKEN = "ENTER_BEARER_TOKEN_HERE"
Paste your Bearer Token inside the quotes.

## 📜 Adding a Wordlist (wordlist.txt)
The script reads usernames from a wordlist file and checks them one by one.

## 📝 How to Create wordlist.txt
Create a file named wordlist.txt in the same folder as script.py
Add usernames, one per line. Example:
Shadow
Gamer
Legend
NightWolf
ProPlayer

Save the file and ensure it's in the same directory as the script.


### ⏳ Adjusting Request Delay
By default, the script waits 0.2 seconds between each request.
You can change the delay to avoid API rate-limiting.

## 🔧 How to Change the Delay
Open script.py
Find this line:
python
Copier
Modifier
DELAY = 0.2  # Lower = faster, higher = safer
Change the number:
Faster requests (Risk of getting blocked): DELAY = 0.1
Safer but slower: DELAY = 0.5
Very safe: DELAY = 1.0


## 🏃‍♂️ Running the Script
Run the script with:
python script.py

The script will start checking usernames and dynamically update the console.

## 📊 Example Output

--
 CHECKED: 7
 VALID:   2
 FAILED:  5
--
[SUCCESS] - Shadow
[SUCCESS] - NightWolf

✔ Valid usernames are shown in green.
❌ Taken usernames are counted but not displayed.

## ❓ FAQ
🔹 Why do I need a Bearer Token?
Wolvesville requires authentication to change usernames. Your token allows the script to check availability.

🔹 How long does the Bearer Token last?
Tokens expire after some time. If the script stops working, get a new Bearer Token using the steps above.

🔹 Can I check usernames randomly instead of using a wordlist?
Yes, you can modify the script to generate random usernames instead.

🔹 Can I check usernames faster?
Yes, but lowering the DELAY too much might get you blocked by the API.

### ⚠️ Disclaimer
This script is for educational purposes only.
Use responsibly and avoid spamming the API.
The script does not guarantee username availability due to potential API restrictions.

