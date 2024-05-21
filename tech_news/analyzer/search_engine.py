from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)

    result = [(new["title"], new["url"]) for new in news]
    return result


# Requisito 8
def search_by_date(date):
    try:
        formatted_date = datetime.strptime(
            date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": formatted_date}
    news = search_news(query)

    result = [(new["title"], new["url"]) for new in news]
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
