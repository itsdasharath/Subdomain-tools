import requests
import argparse
from threading import Thread
import os

def request(url):
    try:
        response = requests.get("http://" + url, timeout=10)
        if response.status_code == 200:
            print(url)
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="SubDomain Enumeration Tool")
    parser.add_argument("-d", "--domain", help="Target domain to enumerate subdomains", required=True)
    parser.add_argument("-w", "--wordlist", help="Path to the subdomain wordlist", default="./wordlists/subdmainwordlist.txt")

    args = parser.parse_args()

    # Check if the wordlist file exists and is readable
    if not os.path.isfile(args.wordlist) or not os.access(args.wordlist, os.R_OK):
        print(f"Error: The wordlist file '{args.wordlist}' does not exist or is not readable.")
        use_default  = input("Do you want to use the default wordlist? (y/n):").strip().lower()

        if use_default == "y":
            args.wordlist = "./wordlists/subdmainwordlist.txt"
            if not os.path.isfile(args.wordlist) or not os.access(args.wordlist, os.R_OK):
                print(f"Error: The default wordlist file '{args.wordlist}' does not exist or is not readable.")
                return
        else:
            print("Exiting...")
            return
    
    print("Discovered SubDomain:")
    threads = []
    try:
        with open(args.wordlist, "r") as wordlist:
            for line in wordlist:
                word = line.strip()
                test_url = f"{word}.{args.domain}"
                t = Thread(target=request, args=(test_url,))
                threads.append(t)
                t.start()
    except Exception as e:
        print(f"Error reading the wordlist file: {e}")
        return
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
