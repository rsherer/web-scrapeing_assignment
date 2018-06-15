import requests
import pymongo from MongoClient
import bs4 from BeautifulSoup

def scrape_site(url, table):
    if not table.find_one({'url': url}):
        response = requests.get(url)
        table.insert_one({'url' : url, 'data' : response.content})
    return table.find_one({'url' : url})