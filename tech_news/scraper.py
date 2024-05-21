import requests
import parsel
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {
        "User-Agent": "Fake user-agent"
    }
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    if not html_content:
        return []

    selector = Selector(html_content)

    news_urls = selector.css("h2.entry-title a::attr(href)").getall()

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    if not html_content:
        return None

    selector = Selector(html_content)

    next_page_url = selector.css("a.next.page-numbers::attr(href)").get()

    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = parsel.Selector(text=html_content)

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = int(
        selector.css(".meta-reading-time::text").re_first(r'\d+'))
    summary = selector.css(".entry-content p").xpath("string()").get().strip()
    category = selector.css(".meta-category .label::text").get()

    news_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category
    }

    return news_data


# Requisito 5
def get_tech_news(amount):
    news = []
    url = "https://blog.betrybe.com/"

    while len(news) < amount:
        html_content = fetch(url)
        updates = scrape_updates(html_content)
        for update in updates:
            if len(news) < amount:
                news_html = fetch(update)
                news_data = scrape_news(news_html)
                news.append(news_data)
            else:
                break
        url = scrape_next_page_link(html_content)
        if not url:
            break

    create_news(news)
    return news
