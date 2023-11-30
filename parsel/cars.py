import asyncio
from db import queries
from db.queries import save_all_cars
from parsel import Selector
import httpx

MAIN_URL = "https://cars.kg"


def get_html(url):
    response = httpx.get(url)
    # print(response.status_code)
    # print(response.text[:250])
    return response.text


def get_title(selector: Selector):
    title = selector.css("title::text").get()
    print(title)


def get_all_catalog_items(selector: Selector):
    items = selector.css('.catalog-list a.catalog-list-item')
    return items


def clear_text(text):
    if text is None:
        return ''

    result = text.strip().replace("\n", "").replace("\t", "")
    result = ' '.join(result.split())
    if result[-1] == ' ,':
        result.replace(' ,', '')
    return result


def main():
    html = get_html(MAIN_URL + '/offers')
    selector = Selector(text=html)
    # get_title(selector)
    items = get_all_catalog_items(selector)
    for item in items:
        title = clear_text(item.css('.catalog-item-caption::text').get())

        descr = clear_text(item.css('.catalog-item-descr::text').get())
        price = clear_text(item.css('.catalog-item-price::text').get())
        url = item.css('::attr(href)').get()
        # print(f'{MAIN_URL}{url}')
        img = clear_text(item.css('.catalog-item-cover img::attr(src)').get())
        # print(img)
        save_all_cars(title, descr, price, url, img)


if __name__ == "__main__":
    queries.init_db()
    main()

