# OSINT Hunter - v1.2 Pro Version (with TruecallerJS)
# By YOU 🔥

import requests
import pyfiglet
import termcolor
import os

def banner():
    os.system('clear')
    ascii_banner = pyfiglet.figlet_format("OSINT Hunter")
    print(termcolor.colored(ascii_banner, 'cyan'))

def search_social(username):
    print(termcolor.colored(f"\n[+] Searching for username: {username}\n", 'yellow'))
    
    platforms = {
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://www.twitter.com/{username}",
        "Telegram": f"https://t.me/{username}",
    }

    for platform, url in platforms.items():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(termcolor.colored(f"✅ {platform} Profile Found: {url}", 'green'))
            else:
                print(termcolor.colored(f"❌ {platform} Profile Not Found", 'red'))
        except:
            print(termcolor.colored(f"❌ Error connecting to {platform}", 'red'))

def google_dork(username):
    print(termcolor.colored("\n[+] Generating Google Dork link...\n", 'yellow'))
    query = f"https://www.google.com/search?q={username}"
    print(termcolor.colored(f"🔍 Google Search: {query}\n", 'cyan'))

def ip_lookup(ip):
    print(termcolor.colored(f"\n[+] Looking up IP: {ip}\n", 'yellow'))
    try:
        url = f"https://ipinfo.io/{ip}/json"
        r = requests.get(url)
        data = r.json()
        for key, value in data.items():
            print(termcolor.colored(f"{key}: {value}", 'cyan'))
    except:
        print(termcolor.colored("❌ Error retrieving IP info", 'red'))

def phone_lookup(phone_number):
    print(termcolor.colored(f"\n[+] Looking up Phone Number via TruecallerJS: {phone_number}\n", 'yellow'))
    try:
        os.system(f"truecallerjs search -n \"{phone_number}\"")
    except:
        print(termcolor.colored("❌ Error running TruecallerJS", 'red'))

def main():
    while True:
        banner()
        print(termcolor.colored("1) Search Username", 'yellow'))
        print(termcolor.colored("2) Lookup IP", 'yellow'))
        print(termcolor.colored("3) Lookup Phone Number (TruecallerJS)", 'yellow'))
        print(termcolor.colored("4) Exit", 'yellow'))

        choice = input(termcolor.colored("\nEnter your choice: ", 'cyan'))

        if choice == "1":
            username = input(termcolor.colored("Enter Username: ", 'cyan'))
            search_social(username)
            google_dork(username)
            input(termcolor.colored("\nPress Enter to continue...", 'yellow'))
        elif choice == "2":
            ip = input(termcolor.colored("Enter IP Address: ", 'cyan'))
            ip_lookup(ip)
            input(termcolor.colored("\nPress Enter to continue...", 'yellow'))
        elif choice == "3":
            phone_number = input(termcolor.colored("Enter Phone Number (with country code, e.g. +880xxxxxxxxxx): ", 'cyan'))
            phone_lookup(phone_number)
            input(termcolor.colored("\nPress Enter to continue...", 'yellow'))
        elif choice == "4":
            print(termcolor.colored("Goodbye!", 'yellow'))
            exit()
        else:
            print(termcolor.colored("Invalid choice!", 'red'))
            input(termcolor.colored("\nPress Enter to continue...", 'yellow'))

if __name__ == "__main__":
    main()