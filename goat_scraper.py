#!/usr/bin/env python
# coding: utf-8

# In[50]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import requests 
from bs4 import BeautifulSoup

import time
from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}


# In[66]:


# make request for the webpage to be saved
request = requests.get('https://goat.com/', headers = user_agent)
source_code = request.text
soup=BeautifulSoup(source_code)

#w rite file 
## not sure if this works as it may get blocked
f = open('goat.html', 'w', encoding = 'utf-8')
f.write(requests.get('https://goat.com', headers =  {'User-agent': 'Mozilla/5.0'}).text)
f.close()


# In[67]:


#save the html as source
driver.page_source


# In[46]:


# Load in product page via selenium
#c hange url based on which page to run
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.goat.com/collections/just-dropped?recently_released=sneakers&sortBy=release_date&sortOrder=descending"
driver.get(url)


# In[40]:


# get all the links for specified page via infinite scroll
time.sleep(2)  # 2 seconds to load the page
scroll_pause_time = 1 # in seconds
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
        

sneaker_urls = []

def get_all_links(url = 'https://www.goat.com/sneakers?release_date_year=1981&release_date_year=2022&release_date_year=2009&release_date_year=1994&gender=infant'):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers = user_agent)
    soup = BeautifulSoup(res.text, "html.parser")

    # return the href attribute in the <a> tag nested within the first product class element
    urls = soup.find_all(class_='GridStyles__GridCellWrapper-sc-1cm482p-0 gRjscl')
    
    
    for sneaker in urls:
        url_sneaker = sneaker.find("a").attrs["href"]
        base_url = "https://goat.com"
        sneaker_url = base_url + url_sneaker
        sneaker_url = sneaker_url.replace('../', '')
        sneaker_urls.append(sneaker_url)
    
    return(sneaker_urls)
          
        
get_all_links() 
len(sneaker_urls)


# In[59]:


# Load in product page via selenium
#c hange url based on which page to run
driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.goat.com/sneakers/dunk-low-black-white-dd1391-100"
driver.get(url)


# In[52]:


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

#product_info = []

#def get_product_info 
#res = driver.page_source.encode("utf-8")      
#soup = BeautifulSoup(driver.page_source)


#user_agent = {'User-agent': 'Mozilla/5.0'}
#res = requests.get(url, headers = user_agent)

#demo_product_urls = product_urls[:5]

#def extract_product_info(product_urls):

    
#for sneaker in sneaker_urls
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

    #return(product_info)

#product_info


# In[64]:


elements = soup.find_all(class_='swiper-slide swiper-slide-duplicate')

el = elements[0]

import re

# see https://docs.python.org/3/library/re.html

 

attributes = str(el)

attr = []

for item in re.findall(r'[>](.+?)[<]', attributes):

    attr.append(item.replace('</i>',''))

attr


# In[63]:


el


# In[26]:


# write csv file

with open("product_description_pre_owned.csv", "w", encoding = 'utf-8', newline='') as csv_file: 
    writer = csv.writer(csv_file, delimiter = ";")
    writer.writerow(["price", "facts", "featured", "featured"])
    no = datetime.now()
    for product in product_info: 
        writer.writerow([product_po[''], product_po[''], product_po[''], product_po[''], product_po[''], product_po[''], product_po[""], now])


# In[ ]:




