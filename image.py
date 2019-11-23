class Image:
    def __init__(mysillyobject, url):
        mysillyobject.url = url
        mysillyobject.type = ''
        mysillyobject.width = ''
        mysillyobject.height = ''
        mysillyobject.alt = ''

    def __repr__(mysillyobject):
        return mysillyobject.url