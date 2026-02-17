import requests 
import os
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
URL= "'''Include your web page URL here'''"
with open("valid_proxies.txt","r") as f:
    proxies = f.read().split("\n")
     

counter = 0 
tries = 0
while tries<len(proxies):
    
    proxy= proxies[counter]
        
    try:
        print(f"Using the proxy: {proxy}")
        response = requests.get(URL,proxies={"http": proxy, 
        "https": proxy},
        headers=headers,timeout=5)
        print(response.status_code)
            
        if response.status_code == 200:
            break

    except:
        print("Failed")
            
    finally:
        counter +=1
        counter= counter % len(proxies)
        tries += 1
            