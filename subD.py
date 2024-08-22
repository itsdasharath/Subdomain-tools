import requests
from threading import Thread

def request(url):
    try:
        response = requests.get("http://" + url, timeout=10)
        if response.status_code == 200:
            print(url)
    except:
        pass

def main():
    target_url = input("Enter Target Domain  : ")
    print("Discovered SubDomain:")
    threads = []
    with open("subdmainwordlist.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            test_url = word + "." + target_url
            t = Thread(target=request, args=(test_url,))
            threads.append(t)
            t.start()
    
    for t in threads:
        t.join()

main()
