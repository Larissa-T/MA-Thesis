from urllib.parse import urlparse

"""
# This part will allow you to crawl all sub domains when such links are presented I wanted to stay within the sub domain as i didn't wanted to crawl the entire university's website
# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
"""

# Get sub domain name (name.example.com)
def get_domain_name(url):#get_sub_domain_name(url): # Perhaps this code is somewhat redundant but I haven't tried running without it
    try:
        return urlparse(url).netloc
    except:
        return ''
