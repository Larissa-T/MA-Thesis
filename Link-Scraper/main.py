import threading
from queue import Queue
try:
    import queue
except ImportError:
    import Queue as queue
#from multiprocessing import Queue
from spiderwithoutssl import Spider     # If you encounter any SSL-errors use the spiderwithssl.py it will skipp the problematic certification which causes the error
from domain import *
from general import *

PROJECT_NAME = 'university_department-subsection'       # Define the folder in which the files will be saved if it doesn't exsist it will automatically make one 
HOMEPAGE = 'start point of the website you want to crawl'   # Fill in here the homepage on which the spider will start crawling
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 16                                  # Depending on the power of your computer and the server you might need to tweak the amount of threads/spiders 16 has been a magic number for me although some websites shut me down which made me roll it back to 2
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
