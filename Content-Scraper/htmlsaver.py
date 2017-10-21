import urllib
import ssl
#from urllib import parse
import urllib
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

uni = 'ucl_'
dept = 'hebrew-dis_'
html_file = uni + dept + '_html.txt'
text_file = uni + dept + '_text.txt'

#load all urls into a list
with open("ucl_5/ucl_hebrew-dis/crawled.txt", "r") as f:
    link_list =[]
    print ('loading list')
    for item in f:
        link_list.append(item)

link_list = [item[:-1] for item in link_list]
print ('made proper list with strings')
filename = html_file

for url in link_list:
    if 'pdf' in url:
        continue
    elif 'ARM_2015-16' in url:
        continue
    elif 'LIS_2015-16' in url:
        continue
    elif 'ppt' in url:
        continue
    elif 'documents' in url:
        continue
    elif 'event' in url:
        continue
    elif 'edit' in url:
        continue
    elif 'people' in url:
        continue
    elif 'news' in url:
        continue
    elif 'docx' in url:
        continue
    elif 'doc' in url:
         continue
    elif 'gif' in url:
        continue
    elif 'jpeg' in url:
        continue
    elif 'jpg' in url:
        continue
    elif 'grad' in url:
        context = ssl._create_unverified_context()
        html = urllib.urlopen(url, context=context).read()
        print ('reading ' + url)
        f = open(filename, "a")
        f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
        f.close()
        print ("done adding html " + url)
    elif 'module' in url:
        context = ssl._create_unverified_context()
        html = urllib.urlopen(url, context=context).read()
        print ('reading ' + url)
        f = open(filename, "a")
        f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
        f.close()
        print ("done adding html " + url)
    elif 'courses' in url:
        context = ssl._create_unverified_context()
        html = urllib.urlopen(url, context=context).read()
        print ('reading ' + url)
        f = open(filename, "a")
        f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
        f.close()
        print ("done adding html " + url)
    elif 'study' in url:
        context = ssl._create_unverified_context()
        html = urllib.urlopen(url, context=context).read()
        print ('reading ' + url)
        f = open(filename, "a")
        f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
        f.close()
        print ("done adding html " + url)
    elif 'taught' in url:
        context = ssl._create_unverified_context()
        html = urllib.urlopen(url, context=context).read()
        print ('reading ' + url)
        f = open(filename, "a")
        f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
        f.close()
        print ("done adding html " + url)
    else:
        continue
print ('saved all html starting to extract')

with open(html_file) as f:
    file = BeautifulSoup(f, "html5lib")

#print (file)
for p_text in file.find_all('p'):
    text = p_text.getText()
    f = open(text_file, "a")
    f.write(text.encode('utf-8'))
    f.close()
print (text)
