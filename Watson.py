import requests
from colorama import init,Fore,Style 

class Watson:
    def __init__(self):
        self.sites = [
            "github.com", "gitlab.com", "bitbucket.org", "dev.to",
            "replit.com", "twitter.com", "tiktok.com", "twitch.tv",
            "kick.com", "dailymotion.com", "medium.com", "dribbble.com",
            "behance.net", "soundcloud.com", "audiomack.com",
            "letterboxd.com", "linkedin.com/in", "ko-fi.com"
        ]
        self.doms = [
            ".com", ".net", ".org", ".blogspot.com",
            ".netlify.app", ".glitch.me", ".hubspot.com"
        ]

    def check_url(self, url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[*] User found on {url}")
                return True
            elif response.status_code == 404:
                return False
            elif response.status_code == 403:
                print(Fore.RED + f"[!!] {url} - Recognized as bot or access forbidden")
                return False
            else:
                print(f"[---] {url} returned status code {response.status_code}")
                return False
        except requests.exceptions.RequestException:
            return False

    def scan_username(self):
        while True:
            username = input("Watson ").strip().lower()
            if not username:
                print("Username cannot be empty.")
                continue

            for site in self.sites:
                url = f"https://{site}/{username}/"
                self.check_url(url)

            for dom in self.doms:
                url = f"https://{username}{dom}"
                self.check_url(url)


if __name__ == "__main__":
    scanner = Watson()
    scanner.scan_username()
