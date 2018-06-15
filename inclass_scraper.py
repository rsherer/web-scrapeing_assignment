import requests
import pymongo
mc = pymongo.MongoClient()
scraper_db = mc['scraper']
sites = scraper_db['sites']


def retrieve_site(url: str) -> bytes:
    for site in sites.find():
        if site['url'] == url:
            return site['data']


def scrape_site(url: str) -> bytes:
    data = retrieve_site(url)
    if data:
        return data
    response = requests.get(url)
    data = response.content
    sites.insert_one({'url': url,
                      'data': data})
    return data
