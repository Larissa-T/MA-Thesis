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
                    if 'login' in url:           # Here I excluded all links that contain the word login, as university websites often contain quicklinks to login pages which will be repeadtly be visited by the crawler. It could be interpeted by the server as an attack which will result in being blacklisted.   
                            continue
                    elif 'calendar' in url:     # This part skips all links containing the word calendar as they are not to my interest aswell as sometimes results into a thread looking at each day in the past as well as future which will go on infinity
                            continue
                    elif 'events' in url:       # This part skips all links containing the word event as they are not to my interest aswell as sometimes results into a thread looking at each day in the past as well as future which will go on infinity
                           continue
                    elif 'ajaxCalendar' in url: # ajaxCalendar is an often used calendar app which will trap your crawler and make it click trough each day in the future as well as in the past
                            continue
                    elif 'search' in url:       # Sometimes the crawler gets into the search box and it gets stuck trying every single search option which will go into infinity
                            continue
                    elif 'social-sciences' in url:  #I am interested in Humanities some university group it together with social sciences this sometimes help skipping the social sciences if the link format is the same
                            continue                # If you want anyhthing else to get skiped simply copy de elif statement (including the continue) and replace anything within the '' with the word you want to be excluded from crawling 
                    elif 'part of url' in url:  #This part defines which links should be added to the list based on a part of the url: For example https://anthropology.stanford.edu/graduate-program if you would like only to have links that contains 'anthropology' then add that word between the ''
                        self.links.add(url)
                    else:
                        continue

    def page_links(self):
        return self.links

    def error(self, message):
        pass
