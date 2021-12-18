import requests
from time import sleep
from colorama import Fore
import win10toast #we notify you every 100 messages

print("BOOTING ... ... ... ... ...")
global n_count
# global count 
toaster = win10toast.ToastNotifier()
count = 0
n_count = 0

print(Fore.RED + """
██████╗░░░░░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔══██╗░░░██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
██║░░██║░░░╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██║░░██║░░░░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝██╗██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚═╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝""" + Fore.RESET)


channel_id = "CHANNEL_ID_HERE"
message = "MESSAGE_HERE"
token = "TOKEN_HERE"
time_out = 1 #TIMEOUT HERE


url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

payload = {
    "content":message
}

headers = {
    "authorization":token
}

for i in range(100001):
    sleep(time_out)
    requests.post(url, data=payload, headers=headers)
    print("Successfully sent a message!")
    if n_count >= 100:
        toaster.show_toast("D.Spammer","100 messages have been sent!", duration=5)
        n_count = 0
    count += 1
    n_count += 1

input("Count: " + str(count))