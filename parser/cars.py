import asyncio
from parsel import Selector
import httpx

MAIN_URL = "https://cars.kg/offers"


def get_html(url):
    response = httpx.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_title(html):
    selector = Selector(text=html)
    title = selector.css("title::text").get()
    print(title)


def main():
    html = get_html(MAIN_URL)
    get_title(html)


if __name__ == "__main__":
    main()
