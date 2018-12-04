#!/usr/bin/env python
from bs4 import BeautifulSoup
from time import sleep
from multiprocessing.dummy import Pool
from urllib.request import urlopen
import time


URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/']

def load_url(url):
	soup = BeautifulSoup(urlopen(url), features="lxml")
	return soup.title.string





if __name__ == '__main__':
	
	print("1 watek")
	start = time.time()
	for u in URLS:
    		print(load_url(u))
	end = time.time()
	print(end - start)

	print("5 watkow")

	start = time.time()
	pool = Pool(4)
	s = pool.map(load_url, URLS)
	pool.close()
	pool.join()
	for i in s:
		print(i)
	end = time.time()
	print(end - start)