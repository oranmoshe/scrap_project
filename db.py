import metadata
import image
import time

db = {}
id_to_url = {}

def contains(url):
    return db.has_key(url)

def update(url,graph):
    m = db.get(url)
    i = image.Image('')
    if(not graph.is_valid()):
        return  None
    for x,y in graph.items():
        print "%-15s => %s" % (x, y)
        if(x=='url'):
            m.url = y
        if(x=='type'):
            m.type = y
        if(x=='title'):
            m.title = y
        if(x=='updated_time'):
            m.updated_time = y
        if(x=='image' or x=='image:url'):
            if(not i.url==''):
                m.images.append(i)
            i = image.Image(y)
        if(x=='image:height'):
            i.height = y
        if(x=='image:width'):
            i.width = y
        if(x=='image:type'):
            i.type = y
        if(x=='image:alt'):
            i.alt = y
    if(not i.url==''):
        m.images.append(i)
    m.scrape_status = 'done'


def add(url):
    if contains(url):
        return get_by_url(url).id
    m = metadata.MetaData(url)
    db[url] = m
    id_to_url[m.id] = url
    return m.id


def get_by_url(url):
    if contains(url):
        return db[url]
    return None

def get_by_id(id):
    if(id_to_url.has_key(id) and contains(id_to_url[id])):
        return db[id_to_url[id]]
    return None