# 🍪🔥 Cookie Tester 🔥🍪

Cookie Tester is a simple Python CLI tool that sends a custom cookie to a target URL
and judges whether the server likes it or not 😈🍪

If the server redirects you — congratulations.
If not — better luck next time.

---

## 👀 Overview

Cookies are everywhere.
Sessions depend on them.
Auth depends on them.
Sometimes access depends on them 👀

Cookie Tester lets you manually test a cookie value against a target URL
and instantly see whether it works or gets rejected.

No browser.
No extensions.
Just pure HTTP behavior.

---

## 🚀 Features

- Accepts a target URL 🌐  
- Accepts a custom cookie value 🍪  
- Sends cookie using HTTP request 📡  
- Detects redirect-based authentication (302) 🔁  
- Clean and simple output 😎  
- Lightweight and beginner-friendly 🪶  

---

## ⚙️ How It Works

The tool sends an HTTP GET request to the target URL
with a user-provided cookie value.

If the server responds with status code 302,
the cookie is considered valid or interesting.

If not, the server was not impressed.

Simple logic.
Clear results.

---

## 🧪 Usage

Run the tool  
python cookietester.py

Enter the target URL when prompted  
Enter the cookie value you want to test

Then let the server decide your fate 😌

---

## 📤 Example Output

Delicious! 🍪🔥  

or  

Sorry, next time bring something better! 😬

No middle ground.

---

## 📦 Requirements

- Python 3.x  
- requests library  

Install requests if needed  
pip install requests

---

## 🧠 What You Learn From This Project

- How cookies are sent in HTTP requests  
- Session testing basics  
- Redirect-based authentication behavior  
- Using Python requests library  
- Why cookies matter in web security  

---

## 🗿 Final Words

Cookies decide access.
Servers don’t lie.
And bad cookies get rejected fast.

Test wisely 🍪😈
