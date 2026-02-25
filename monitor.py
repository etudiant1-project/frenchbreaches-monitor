import requests
import os
import sys

URL = "https://frenchbreaches.com/"
KEYWORD = os.getenv("KEYWORD", "example.com")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))

def check_site():
    print(f"Checking {URL} for keyword: {KEYWORD}")

    try:
        response = requests.get(URL, timeout=TIMEOUT)
        response.raise_for_status()

        if KEYWORD.lower() in response.text.lower():
            print(f"[ALERT] Keyword '{KEYWORD}' FOUND!")
            sys.exit(1)  # utile pour CronJob (status d'échec)
        else:
            print(f"[OK] Keyword '{KEYWORD}' not found.")
            sys.exit(0)

    except requests.RequestException as e:
        print(f"[ERROR] HTTP error: {e}")
        sys.exit(2)

if __name__ == "__main__":
    check_site()
