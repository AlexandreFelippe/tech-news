import requests
import time


# Requisito 1
def fetch(url):
    time.sleep(3)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None

    if __name__ == "__main__":
        url = "https://blog.betrybe.com"
        html = fetch(url)
        print(html[:500])


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
