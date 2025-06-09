# OSINT Hunter 🔎

**OSINT Hunter** is a powerful and lightweight Open-Source Intelligence (OSINT) tool built using **Python** and **TruecallerJS**.

It helps you gather publicly available information about:
- Usernames 👤  
- IP Addresses 🌐  
- Phone Numbers 📞  

in an easy and automated way.  
Perfect for **ethical hackers**, **cybersecurity researchers**, **investigators**, and **students** who want to explore the world of OSINT 🚀.

---

## Features ✨

✅ Username Search → Check username presence on popular platforms  
✅ IP Lookup → Find details about public IP addresses (location, ISP, etc.)  
✅ Phone Number Lookup → Get Name, Carrier, Location using **TruecallerJS**  
✅ Beautiful CLI Interface with Colorful Outputs  

---

## Installation 📥

### Requirements:

- Python 3
- NodeJS
- Git
- Pip

### Setup:

```bash
# Clone this repository
git clone https://github.com/yourusername/osint-hunter.git
cd osint-hunter

# Install Python dependencies
pip install -r requirements.txt

# Install TruecallerJS globally
npm install -g truecallerjs

# Login once with TruecallerJS to save token
truecallerjs login

# Run OSINT Hunter
python3 osint.py
