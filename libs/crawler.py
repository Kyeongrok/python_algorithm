import requests

def crawl(url):
    data = requests.get(url)
    print(data.status_code)
    return data.content
