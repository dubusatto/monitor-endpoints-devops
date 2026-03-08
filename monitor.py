import requests

URLS = ["https://google.com", "https://github.com"]

def check_endpoints():
    for url in URLS:
        response = requests.get(url)
        print(f"Site: {url} | Status: {response.status_code}")

if __name__ == "__main__":
    check_endpoints()