import threading
import queue

import requests

q = queue.Queue()

with open("all-proxies.txt","r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)
        
        
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            request = requests.get("https://ipinfo.io/json", proxies={
                "http": proxy, "https": proxy
            },timeout=5)
        except:
            continue
        if request.status_code == 200:
            print(proxy)
            with open("valid_proxies.txt","a") as f:
                f.write(proxy+"\n")
            
for th in range(10):
    threading.Thread(target=check_proxies).start()