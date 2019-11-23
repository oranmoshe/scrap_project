from datetime import datetime
import hashlib
import json

class MetaData:
    def __init__(mysillyobject, url):
        mysillyobject.id = hashlib.md5(url).hexdigest()
        mysillyobject.url = url
        mysillyobject.images = []
        mysillyobject.type = ''
        mysillyobject.title = ''
        mysillyobject.updated_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        mysillyobject.scrape_status = "pending"

    def __repr__(mysillyobject):
        return str(mysillyobject.id)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)