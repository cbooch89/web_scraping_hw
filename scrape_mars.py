# Importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pymongo
import requests
import pandas as pd
from flask import Flask, render_template
from selenium import webdriver

def init_browser():
    # splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=True)

#----------------------Mars articles-----------------------------
def scrape_info():
    browser = init_browser()
        
    # Mars News Url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)
#scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

#####info going on page
    results = soup.find_all('div', class_="slide")
    
    for result in results:
        headlines = result.find('div', class_="content_title")
        title = headlines.find('a').text
        
        article_body = result.find('div', class_="rollover_description")
        
        body = article_body.find('div', class_="rollover_description_inner").text
    


#------------------------Mars images-----------------------------
    url_mars_pic = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_mars_pic)
    time.sleep(2)
#scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    #pull image from site
    images = soup.find_all('a', class_="fancybox")

    #new featured image from site
    featured_image_list = []
    for image in images:
        full_size = image['data-fancybox-href']
        featured_image_list.append(full_size)

    ####info going on page
        featured_image_url = "https://www.jpl.nasa.gov/" + full_size

    #-----------------------weather------------------------
        #url and BS
    url_Weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_Weather)
    time.sleep(1)
    #scrape page into soup
    html = browser.html
    soup = bs(html,'html.parser')

    weather = soup.find_all("div",class_="js-tweet-text-container")

    mars_weather = []
    for content in weather:
        info = content.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        mars_weather.append(info)

    #####info going on page
        current_weather = mars_weather[0]

    # #----------------------Mars facts----------------------------------

    #url to df
    url_table = "https://space-facts.com/mars/"
    table = pd.read_html(url_table)[0]

        #setting up table/df
    table.columns = ['Mars - Earth Comparison','Mars','Earth']
    mars_table = table.copy()
    # mars_table.set_index(['Mars - Earth Comparison'])

        #html table
    mars_facts = mars_table.to_html()
    mars_facts = mars_facts.replace("\n","")

    #####info going on page
    Mars_fact_table =mars_facts

    #-------------------------mars hemispheres-----------------------
        
    # url and BS
    url_Hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_Hemi)
    time.sleep(1)
    html = browser.html
    soup = bs(html,'html.parser')

    #creating hemi image title list and pulling from site
    hemi_title_list = []
    for img_title in soup.find_all('div',class_="description"):
        hemi_title_list.append(img_title.find('h3').text)
        
        hemi_thumb_img_list=[]
        
        for image in soup.find_all('div', class_='item'):
            url = "https://astrogeology.usgs.gov/"
            hemi_thumb_img_list.append(url + image.find('img').get('src'))

    #stripping thumbnail and adding full image tag
    full_img_list=[]
    for all_url in hemi_thumb_img_list:
        split_thumb= all_url.split('.tif_thumb.png')
        full_tag = split_thumb+'.tif/full.jpg'
        full_img_list.append(full_tag)

    #string together
    mars_hemi_info = [
        {"title": "Valles Marineris Hemisphere", "img_url": full_img_list[3]},
        {"title": "Cerberus Hemisphere", "img_url": full_img_list[0]},
        {"title": "Schiaparelli Hemisphere", "img_url": full_img_list[1]},
        {"title": "Syrtis Major Hemisphere", "img_url": full_img_list[2]},
    ]
    #####info going on page
    mars_hemi_info = hemi_title_list

    #--------------------------------------------------------------
    infomation = {
        "title": title,
        "boby": body,
        "featured_image_url": featured_image_url,
        "current_weather": current_weather,
        "Mars_fact_table": Mars_fact_table,
        "mars_hemi_info": mars_hemi_info,

    }
    
    # Close the browser after scraping
    browser.quit()

        # Return results
    return infomation