#!/usr/bin/env python
# coding: utf-8

# In[48]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import requests 
from bs4 import BeautifulSoup

import time
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}


# In[49]:


# make request for the webpage to be saved
request = requests.get('https://goat.com/', headers = user_agent)
source_code = request.text
soup=BeautifulSoup(source_code)

#w rite file 
## not sure if this works as it may get blocked
f = open('goat.html', 'w', encoding = 'utf-8')
f.write(requests.get('https://goat.com', headers =  {'User-agent': 'Mozilla/5.0'}).text)
f.close()


# In[70]:


# Load in product page via selenium
#c hange url based on which page to run
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.goat.com/brand/air-jordan?recently_released=sneakers&sortBy=release_date&sortOrder=descending&release_date_year=2022"
driver.get(url)


# In[71]:


# get all the links for specified page via infinite scroll
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1


while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break 
        


def get_all_links(url = 'https://www.goat.com/brand/air-jordan?sortBy=relevance&sortOrder=descending'):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers = user_agent)
    soup = BeautifulSoup(res.text, "html.parser")

    # return the href attribute in the <a> tag nested within the first product class element
    urls = soup.find_all(class_='GridStyles__GridCellWrapper-sc-1cm482p-0 gRjscl')
    
    
    
    sneaker_urls = []
    for book in urls:
        url_sneaker = book.find("a").attrs["href"]
        base_url = "https://goat.com"
        sneaker_url = base_url + url_sneaker
        sneaker_url = sneaker_url.replace('../', '')
        sneaker_urls.append(sneaker_url)
    
    return(sneaker_urls)
        
    
        

get_all_links() 


# In[56]:


## Scrape product page

# scrape price point  per size
# scrape facts page
# release date
# SKU
# Colorway
# Main color
# Upper material
# Technology
# Category
soup = BeautifulSoup(driver.page_source)

for el in soup.find_all(class_ = 'swiper-slide swiper-slide-duplicate'):
    price = el.find('span')
    if price is not None: print(price.text)

for el in soup.find_all(class_ = 'WindowItemShortText__Right-sc-jrzdw-2 cFFSIe'):
    facts = el.find('span')
    if price is not None: print(facts.text)


for el in soup.find_all(class_ = 'WindowItemFeaturedIn__Collections-sc-81rn64-3 fyXtSW'):
    featured = el.find('a') 
    if price is not None: print(featured.text) 
        
        
for el in soup.find_all(class_ = 'ProductInfo__Container-sc-yvcr9v-1 cUuIBo'):
    featured = el.find('h1') 
    if price is not None: print(featured.text) 

