import requests
from bs4 import BeautifulSoup
import random
import sys
import urllib.request

def get_soup(url):
    site = requests.get(url)
    page = site.text
    return BeautifulSoup(page, 'lxml')

query = input("search:\n")
target_site = "https://wallhaven.cc/search?q={}&page=2".format(query)

soup2 = get_soup(target_site)
img_arr = (soup2.findAll('img'))[0:50]      #returns a list with all the img attributes

final_img = BeautifulSoup()
try:
    final_img1 = random.choice(img_arr[1:])
    
    final_img = final_img1.attrs['data-src']
    
except IndexError:
    print("search results don't exist")
    sys.exit(1)

print(final_img)    #for printing image url in console
img_response = requests.get(final_img, stream = True)
img_data = img_response.content

filename = str(query) + "_pic"
with open(filename + ".jpg", "wb") as handler:
    handler.write(img_data)
