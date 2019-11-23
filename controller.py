import opengraph
import requests
import db
import threading
import Queue
from bs4 import BeautifulSoup

q = Queue.Queue()

def get_metadata(id):
    return db.get_by_id(id)


def get_id(url):
    if not db.contains(url):
        q.put(url)
    return db.add(url)


def find_canonical_beautiful_soup(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        page = requests.get(url,headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if(soup):
            canonical = soup.find('link', {'rel': 'canonical'})
        return canonical['href']
    except requests.exceptions.RequestException as e:
        print (e)
    return None


def scrap(url):
    print ('work!')
    og = opengraph.OpenGraph(url=url)
    db.update(url, og)
    print (og)

def worker():
    while True:
        item = q.get()
        scrap(item)
        q.task_done()
for i in range(4):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()
