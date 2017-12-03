import urllib
import ssl
#from urllib import parse
import urllib
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

uni = 'ucl_'                            # Define a short code for the university name (change to what you like) becomes part of the filename
dept = 'hebrew-dis_'                    # DEFINE a short code for the department name (change to what you like) becomes part of the filename
html_file = uni + dept + '_html.txt'
text_file = uni + dept + '_text.txt'

#load all urls into a list
with open("path/path/path/file.txt", "r") as f:
    link_list =[]
    print ('loading list')
    for item in f:
        link_list.append(item)
# As the link list created by the Link-Scraper has after each link /n this part will scrape it of so we won't get any html 404 errors
link_list = [item[:-1] for item in link_list]
print ('made proper list with strings')
filename = html_file

for url in link_list:
    if 'pdf' in url:        # The first part excludes any links that will open documents of which the html cannot be extracted as well as type of pages (such as people, news and events) 
        continue            # which will definitly not include course or program description however do have trigger words such as courses, seminar, undergraduate, program
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
    elif 'grad' in url:             # this part onwards tells what to do when certain words are present within the url view the link list before defining which links should be added here 'grad' is used to both capture the links containing graduate as undergraduate and I have seen sometimes just grad is being used in links that contain program descriptions 
        context = ssl._create_unverified_context()          #skipps any ssl certification
        try: 
            html = urllib.urlopen(url, context=context).read()  #opens the links and grabs the html
        except IOError or UnicodeError:         #skips url if it comes across any errors
            print ('cannot open page')
        else:
            print ('reading ' + url)
            f = open(filename, "a")     # opens the filename to append
            try:
                 f.write(url + " /n" + html.encode('utf-8', errors='ignore'))   #writes first the url in order to track where the html came from and then writes the html. 
            except UnicodeError:        #I have added the unicodeerror handeler in case of trouble writing or accidentaly rtying to write an image as text it will simply skip the part that causes the error
                print('error')
            else:
                f.close()
    elif 'module' in url:
       context = ssl._create_unverified_context()
        try:
            html = urllib.urlopen(url, context=context).read()
        except IOError or UnicodeError:
            print ('cannot open page')
        else:
            print ('reading ' + url)
            f = open(filename, "a")
            try:
                f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
            except UnicodeError:
                print('error')
            else:
                f.close()
        print ("done adding html " + url)
    elif 'courses' in url:
        context = ssl._create_unverified_context()
        try:
            html = urllib.urlopen(url, context=context).read()
        except IOError or UnicodeError:
            print ('cannot open page')
        else:
            print ('reading ' + url)
            f = open(filename, "a")
            try:
                f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
            except UnicodeError:
                print('error')
            else:
                f.close()
        print ("done adding html " + url)
    elif 'study' in url:
       context = ssl._create_unverified_context()
        try:
            html = urllib.urlopen(url, context=context).read()
        except IOError or UnicodeError:
            print ('cannot open page')
        else:
            print ('reading ' + url)
            f = open(filename, "a")
            try:
                f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
            except UnicodeError:
                print('error')
            else:
                f.close()
        print ("done adding html " + url)
    elif 'taught' in url:
        context = ssl._create_unverified_context()
        try:
            html = urllib.urlopen(url, context=context).read()
        except IOError or UnicodeError:
            print ('cannot open page')
        else:
            print ('reading ' + url)
            f = open(filename, "a")
            try:
                f.write(url + " /n" + html.encode('utf-8', errors='ignore'))
            except UnicodeError:
                print('error')
            else:
                f.close()
        print ("done adding html " + url)
    else:
        continue
print ('saved all html starting to extract')
#if you have a very long url list you might want to copy the next part of code which does the text extraction to a seperate file so it won't take hours running the entire code
with open(html_file) as f:
    file = BeautifulSoup(f, "html5lib") # Opens the file in which all the html has been saved by the code above 
                                        # working on MAC you might want to switch the html5lib for lxml as html5lib install causes errors
#print (file)
for p_text in file.find_all('p'):       # extracts all text between <p></p> allthough visable text can also occur between other tags up until now I have not encountered it as a problem
    text = p_text.getText()
    f = open(text_file, "a")
    f.write(text.encode('utf-8'))
    f.close()
print (text)    # Somehow it doesn't print the entire text of the file but only the last part (1 or 2 lines) however it does when this part of the code is in a seperate file
                # it is not bad I only added it as a sort of visual marker that something has been saved into the file so I don't have to open the file to check it after the code is finished
