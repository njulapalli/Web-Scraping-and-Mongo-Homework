
# coding: utf-8

# # Mission to Mars

# In[11]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd

def scrape(): 

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)


    # In[8]:


    # Define database and collection
    db = client.mars_db
    collection = db.items


    # ## Step 1 - Scraping
    # ### NASA Mars News
    # 

    # In[9]:


    #Creating mars data dictionary and adding each section of the assignment to mars data.
    # mars data dictionary will be added to mongodb in flask app and displayed using bootstrap
    mars_data = {}

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('div', class_='slide')
    results[0]


    # In[10]:


    news_title = results[0].find('div', class_='content_title').find('a').text
    print(news_title)

    news_p = results[0].find('div', class_='rollover_description_inner').text
    print(news_p)

    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p


    # ### JPL Mars Space Images - Featured Image

    # In[11]:


    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('section', class_='centered_text clearfix main_feature primary_media_feature single')
    featured_image_url = "https://www.jpl.nasa.gov" + results[0].find('a', class_='button fancybox').get("data-fancybox-href")

    mars_data['featured_image_url'] = featured_image_url


    # ### Mars Weather
    # 

    # In[12]:


    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('div', class_='content')

    mars_weather = ""
    for result in results:
        if "Mars Weather" in result.find('div', class_='stream-item-header').text:
            mars_weather = result.find('div', class_='js-tweet-text-container').text

    print(mars_weather)
    mars_data['mars_weather'] = mars_weather 


    # ### Mars Facts

    # In[13]:


    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['', 'Values']
    df.set_index('', inplace=True)
    mars_data['mars_facts'] = df.to_html() 


    # ### Mars Hemispheres

    # In[14]:


    # Visit the USGS Astrogeology site 
    # https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    # to obtain high resolution images for each of Mar's hemispheres.

    # Above link is not working so using 4 separate links to obtain images
    hemisphere_image_urls = []


    # In[15]:


    # Cerberus Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('img', class_='wide-image')
    img_url = "https://astrogeology.usgs.gov/" + results[0].get("src")
    title = soup.find_all('h2', class_='title')[0].text

    hemidict = {}
    hemidict["title"] = title
    hemidict["img_url"] = img_url

    hemisphere_image_urls.append(hemidict)
    hemisphere_image_urls


    # In[16]:


    # Schiaparelli Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('img', class_='wide-image')

    title = soup.find_all('h2', class_='title')[0].text
    print(title)

    img_url = "https://astrogeology.usgs.gov/" + results[0].get("src")
    print(img_url)

    hemidict = {}
    hemidict["title"] = title
    hemidict["img_url"] = img_url

    hemisphere_image_urls.append(hemidict)


    # In[17]:


    # Cerberus Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('img', class_='wide-image')

    title = soup.find_all('h2', class_='title')[0].text
    print(title)

    img_url = "https://astrogeology.usgs.gov/" + results[0].get("src")
    print(img_url)

    hemidict = {}
    hemidict["title"] = title
    hemidict["img_url"] = img_url

    hemisphere_image_urls.append(hemidict)


    # In[18]:


    # Syrtis Major Hemisphere
    url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse s 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('img', class_='wide-image')

    title = soup.find_all('h2', class_='title')[0].text
    print(title)

    img_url = "https://astrogeology.usgs.gov/" + results[0].get("src")
    print(img_url)

    hemidict = {}
    hemidict["title"] = title
    hemidict["img_url"] = img_url

    hemisphere_image_urls.append(hemidict)


    # In[19]:


    mars_data['hemisphere_image_urls'] = hemisphere_image_urls
    hemisphere_image_urls

    return mars_data

