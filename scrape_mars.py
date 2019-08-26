# Importing dependencies
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests
from flask import Flask, render_template
import time
import numpy as np
import json
from selenium import webdriver

def init_browser():
    # splinter
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)
    
#Mars articles
def scrape():
    browser = init_browser()
    infomation = {}
    
    # Mars News Url
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup1 = BeautifulSoup(html, 'html.parser')

    infomation["title"] =soup.find_all('div', class_="content_title").get_text()
    infomation["body"] = soup.find_all('div', class_="rollover_description").get_text()


#Mars images
    url_mars_pic = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_mars_pic)
    time.sleep(1)
    html = browser.html
    soup2 = BeautifulSoup(html,'html.parser')

#pull image from site
images = soup2.find_all('a', class_="fancybox")

#new featured image from site
featured_image_list = []
for image in images:
    full_size = image['data-fancybox-href']
    featured_image_list.append(full_size)

    infomation["featured_image_url"]= "https://www.jpl.nasa.gov/" + featured_image_list[4]

#weather
    # url and BS
url_Weather = "https://twitter.com/marswxreport?lang=en"
response = requests.get(url_Weather)
soup = BeautifulSoup(response.text, 'html.parser')

weather = soup.find_all("div",class_="js-tweet-text-container")

mars_weather = []
for content in weather:
    info = content.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather.append(info)
    infomation["current_weather"] = mars_weather[0]

#Mars facts

#url to df
url_table = "https://space-facts.com/mars/"
table = pd.read_html(url_table)[0]

    #setting up table/df
table.columns = ['Mars - Earth Comparison','Mars','Earth']
mars_table.set_index(['Mars - Earth Comparison'])
    #html table
mars_facts = mars_table.to_html()
mars_facts = mars_facts.replace("\n","")
infomation['Mars_fact_table']=mars_facts

#mars hemispheres
    
# url and BS
url_Hemi = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_Hemi)
time.sleep(1)
html = browser.html
soup = BeautifulSoup(html,'html.parser')
#creating hemi image title list and pulling from site
hemi_title_list = []
for img_title in soup.find_all('div',class_="description"):
    hemi_title_list.append(img_title.find('h3').text)

#stripping thumbnail and adding full image tag
full_img_list=[]
for all_url in hemi_thumb_img_list:
    split_thumb= all_url.split('.tif_thumb.png')[0]
    full_tag = split_thumb+'.tif/full.jpg'
    full_img_list.append(full_tag)

#string together
mars_hemi_info = [
    {"title": "Valles Marineris Hemisphere", "img_url": full_img_list[3]},
    {"title": "Cerberus Hemisphere", "img_url": full_img_list[0]},
    {"title": "Schiaparelli Hemisphere", "img_url": full_img_list[1]},
    {"title": "Syrtis Major Hemisphere", "img_url": full_img_list[2]},
]
infomation['mars_hemi_info']= hemi_title_list
browser.quit()
