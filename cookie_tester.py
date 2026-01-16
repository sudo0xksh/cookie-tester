print("=========================================")
print("Welcome to Cookie Tester\n")

import requests

url = input("Enter the URL: ")
cookie_value = input("Enter your cookie: ")

cookies = {"session": cookie_value}

resp = requests.get(url, cookies=cookies, allow_redirects=False)

if resp.status_code == 302:
    print("Delicious!")
else:
    print("Sorry, next time bring something better!")

print("\n=========================================")
print("Test Completed")
print("Developed by sudo_0xksh")