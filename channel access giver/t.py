import requests
import time
import os
os.system("cls")
print("[+] XIN channel message sending access giver FORCER TOOL CREATOR")
print("[+] WARNING: DO NOT CHANGE THE FILE NAME.")
print("[+] made by XIN#4090")
time.sleep(1)
print("[+] make sure to share your screen to allow reading messages for the other person")
print("[+] make sure to input the correct discord token so the person can send messages")
time.sleep(1)
print("details:")
print("[+] user cant check token")
print("[+] user cant read messages thru this tool")
print("[+] user can send any message thru this tool only way of stopping them is changing ur password which resets ur token to stop the tool from working")
input("[+] click [ENTER] to continue....")
os.system("cls")
t = input("[+] input token -> ")
u = input("[+] input channel id (example 969650758821769287) -> ")


response = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": t})
if response.status_code == 200:
    os.system("cls")
    print("[+] token is correct creating file now check in 1 minute max and a exe file called gc.exe will be made in a folder called dist")
    x = open("data.txt","rt")
    data = x.read()
    data = data.replace("discordtoken",t)
    data = data.replace("discorduser",u)
    o = open("gc.py","a")
    o()
    f = open("gc.py","wt")
    f.write(data)
    os.system("cls")
    os.system("pyinstaller --onefile gc.py")
    os.system("cls")
    os.remove("gc.py")
    x.close()
    f.close()
    print("[+] created gc.exe")
else:
    print("[+] token is incorrect")

