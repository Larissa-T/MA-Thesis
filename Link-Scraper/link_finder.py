from html.parser import HTMLParser
#from htmllib import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    if 'login' in url:
                            continue
                    elif 'calendar' in url:
                            continue
                    elif 'events' in url:
                           continue
                    elif 'ajaxCalendar' in url:
                            continue
                    elif 'search' in url:
                            continue
                    elif 'social-sciences' in url:
                            continue
                    elif 'trinity' in url:
                        self.links.add(url)
                    else:
                        continue

    def page_links(self):
        return self.links

    def error(self, message):
        pass
