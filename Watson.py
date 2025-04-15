
import requests

def Watson(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            print(f"[*]User found on {url}")
            return True
        elif response.status_code == 404:
            pass
            return False
        elif response.status_code == 403:
           print(f"!!{url} Recognized as bot")
           return False
        else:
            print(f"---The URL {url} returned status code {response.  status_code}.")
            return False
    except requests.exceptions.RequestException as e:
        print("---")
        return False

# Example usage
while True:
  
    username= input("Watson ")
    sites = [
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "dev.to",
    "replit.com",
    "twitter.com",
    "tiktok.com",
    "twitch.tv",
    "kick.com",
    "dailymotion.com",
    "medium.com",
    "dribbble.com",
    "behance.net",
    "artstation.com",
    "soundcloud.com",
    "audiomack.com",
    "letterboxd.com",
    "linkedin.com/in",
    "ko-fi.com"
    
    
    ]   
    doms =[".com",".net",".org",".blogspot.com",".netlify.app",".glitch. me",".hubspot.com"]

    for site in sites:
      try:
      	url = "https://" + site.lower() + "/" + username.lower() + "/"
      	Watson(url)
      
      except:
      	print("error")
    for dom in doms:
      		try:
      			url =  "https://" + username.lower() + dom
      			Watson(url)
      		except:
      			print("error")
    
