{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 1.A - Scraping for Headline info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dependencies\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import time \n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "#chromdriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "#URL AND BS\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)\n",
    "time.sleep(1)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "# find news headings \n",
    "article_list = []\n",
    "for article in soup.find_all('div',class_=\"content_title\"):\n",
    "    article_list.append(article.find('a').text)\n",
    "#article_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pargraph info\n",
    "article_info = []\n",
    "for article in soup.find_all('div',class_=\"article_teaser_body\"):\n",
    "    article_info.append(article.text)\n",
    "#article_info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Headline': \"Robotic Toolkit Added to NASA's Mars 2020 Rover\",\n",
       " 'Details': \"The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. \"}"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#lastest news\n",
    "latest_title = article_list[0]\n",
    "latest_info = article_info[0]\n",
    "News = {\"Headline\": latest_title,\"Details\": latest_info}\n",
    "News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Robotic Toolkit Added to NASA's Mars 2020 Rover\""
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "News['Headline']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Curiosity Mars Rover Finds a Clay Cache\n"
     ]
    }
   ],
   "source": [
    "news = headline.find('div', class_ = 'content_title').text.strip()\n",
    "print (news)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title: Robotic Toolkit Added to NASA's Mars 2020 Rover\n",
      "-----------------------------------------------------------\n",
      "Info on Article: The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. The bit carousel, which lies at the heart of the rover's Sample Caching System, is now aboard NASA's newest rover. \n"
     ]
    }
   ],
   "source": [
    "print(\"Title:\",latest_title)\n",
    "print('-----------------------------------------------------------')\n",
    "print(\"Info on Article:\",latest_info)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 1.B - Pulling images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL and BS\n",
    "url_mars_pic = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url_mars_pic)\n",
    "time.sleep(1)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['/spaceimages/images/wallpaper/PIA23384-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23383-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23382-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23348-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23347-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23346-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23381-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23370-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23369-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23368-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23367-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23366-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23365-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23364-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23363-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23362-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23344-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23361-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23337-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23336-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23335-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23334-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23333-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23341-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23331-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23330-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23329-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23328-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23327-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23325-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23324-640x350.jpg',\n",
       " '/spaceimages/images/wallpaper/PIA23323-640x350.jpg']"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#new featured image from site\n",
    "featured_image_list = []\n",
    "\n",
    "for image in soup.find_all('div',class_=\"img\"):\n",
    "    featured_image_list.append(image.find('img').get('src'))\n",
    "featured_image_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "newst_image_url= featured_image_list[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature Image URL: https://www.jpl.nasa.gov//spaceimages/images/wallpaper/PIA23384-640x350.jpg\n"
     ]
    }
   ],
   "source": [
    "#finally the feature image url\n",
    "feature_Image_url = \"https://www.jpl.nasa.gov/\" + newst_image_url\n",
    "print(\"Feature Image URL:\", feature_Image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 1.C - Get Weather from Twitter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "# url and BS\n",
    "url_Mars_Weather = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url_Mars_Weather)\n",
    "time.sleep(1)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['InSight sol 258 (2019-08-18) low -100.0ºC (-148.1ºF) high -26.2ºC (-15.2ºF)\\nwinds from the SSE at 5.3 m/s (11.9 mph) gusting to 16.8 m/s (37.6 mph)\\npressure at 7.60 hPapic.twitter.com/5nCVjcsmlZ',\n",
       " 'InSight sol 257 (2019-08-17) low -100.2ºC (-148.4ºF) high -26.5ºC (-15.7ºF)\\nwinds from the SSE at 4.4 m/s (9.8 mph) gusting to 17.1 m/s (38.2 mph)\\npressure at 7.60 hPapic.twitter.com/hBQzJWARH0',\n",
       " 'InSight sol 256 (2019-08-16) low -101.7ºC (-151.1ºF) high -25.6ºC (-14.2ºF)\\nwinds from the SW at 4.2 m/s (9.4 mph) gusting to 17.9 m/s (40.0 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 255 (2019-08-15) low -100.1ºC (-148.1ºF) high -24.7ºC (-12.4ºF)\\nwinds from the SSW at 4.5 m/s (10.0 mph) gusting to 17.3 m/s (38.6 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 254 (2019-08-14) low -99.3ºC (-146.7ºF) high -25.9ºC (-14.6ºF)\\nwinds from the SE at 4.9 m/s (10.9 mph) gusting to 18.1 m/s (40.5 mph)\\npressure at 7.60 hPa',\n",
       " '\"Dusty\" the Earthbound twin (triplet?) of @MarsRovers  Opportunity & Spirit is heading for a new home at the National @airandspace Museum.https://twitter.com/AstroStaab/status/1162103864608169984\\xa0…',\n",
       " 'InSight sol 253 (2019-08-13) low -100.0ºC (-148.1ºF) high -25.5ºC (-13.9ºF)\\nwinds from the SSE at 4.6 m/s (10.3 mph) gusting to 16.4 m/s (36.6 mph)\\npressure at 7.60 hPapic.twitter.com/OnwaHAaYRH',\n",
       " 'InSight sol 252 (2019-08-12) low -100.8ºC (-149.4ºF) high -26.0ºC (-14.8ºF)\\nwinds from the SSW at 4.4 m/s (9.8 mph) gusting to 18.3 m/s (40.9 mph)\\npressure at 7.60 hPapic.twitter.com/WY3JQBXVuU',\n",
       " 'I’d say a plutonium-238 powered RTG qualifies the Curiosity and Mars2020 rovers as alternative fuel vehicles. You can explore these and other missions, rockets and more with JPL’s Spacecraft AR for IOS and Androhttps://www.jpl.nasa.gov/apps/pic.twitter.com/f4SheTlQyY',\n",
       " 'InSight sol 251 (2019-08-11) low -101.0ºC (-149.7ºF) high -26.5ºC (-15.8ºF)\\nwinds from the SSE at 4.1 m/s (9.2 mph) gusting to 17.5 m/s (39.1 mph)\\npressure at 7.60 hPapic.twitter.com/9mgFzHl8t3',\n",
       " 'InSight sol 250 (2019-08-10) low -100.0ºC (-148.1ºF) high -26.2ºC (-15.1ºF)\\nwinds from the SSE at 4.4 m/s (9.8 mph) gusting to 16.2 m/s (36.2 mph)\\npressure at 7.60 hPapic.twitter.com/9sZRRUi3dm',\n",
       " 'InSight sol 249 (2019-08-09) low -98.8ºC (-145.8ºF) high -26.0ºC (-14.8ºF)\\nwinds from the SSE at 4.4 m/s (9.8 mph) gusting to 17.5 m/s (39.1 mph)\\npressure at 7.60 hPapic.twitter.com/jDOsvHTwYg',\n",
       " 'InSight sol 248 (2019-08-08) low -99.6ºC (-147.3ºF) high -25.8ºC (-14.4ºF)\\nwinds from the SSE at 4.5 m/s (10.0 mph) gusting to 16.7 m/s (37.3 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 247 (2019-08-07) low -100.4ºC (-148.7ºF) high -26.5ºC (-15.8ºF)\\nwinds from the SSE at 4.6 m/s (10.3 mph) gusting to 16.8 m/s (37.6 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 246 (2019-08-06) low -99.4ºC (-146.8ºF) high -26.5ºC (-15.7ºF)\\nwinds from the SSE at 5.3 m/s (11.7 mph) gusting to 18.1 m/s (40.4 mph)',\n",
       " 'InSight sol 245 (2019-08-05) low -99.9ºC (-147.8ºF) high -25.6ºC (-14.1ºF)\\nwinds from the SSE at 4.6 m/s (10.2 mph) gusting to 17.7 m/s (39.5 mph)\\npressure at 7.60 hPapic.twitter.com/kLqykpNHtR',\n",
       " 'InSight sol 244 (2019-08-03) low -100.3ºC (-148.6ºF) high -27.1ºC (-16.8ºF)\\nwinds from the SSE at 4.4 m/s (9.9 mph) gusting to 15.9 m/s (35.6 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 243 (2019-08-02) low -99.8ºC (-147.7ºF) high -25.9ºC (-14.7ºF)\\nwinds from the SSE at 4.5 m/s (10.1 mph) gusting to 17.1 m/s (38.2 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 242 (2019-08-01) low -99.1ºC (-146.4ºF) high -26.1ºC (-15.0ºF)\\nwinds from the SW at 4.7 m/s (10.5 mph) gusting to 17.1 m/s (38.2 mph)\\npressure at 7.60 hPa',\n",
       " 'InSight sol 241 (2019-07-31) low -100.5ºC (-148.9ºF) high -26.2ºC (-15.2ºF)\\nwinds from the SSE at 4.6 m/s (10.2 mph) gusting to 16.2 m/s (36.2 mph)\\npressure at 7.60 hPa']"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#pulling all weather to see newst\n",
    "weather_list = []\n",
    "# for weather in soup.find_all('span', class_ = \"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0\"):\n",
    "#     weather_list.append(weather.text)\n",
    "    \n",
    "for weather in soup.find_all('p',class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\"):\n",
    "    weather_list.append(weather.text)\n",
    "weather_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Latest Mars Weather: InSight sol 258 (2019-08-18) low -100.0ºC (-148.1ºF) high -26.2ºC (-15.2ºF)\n",
      "winds from the SSE at 5.3 m/s (11.9 mph) gusting to 16.8 m/s (37.6 mph)\n",
      "pressure at 7.60 hPapic.twitter.com/5nCVjcsmlZ\n"
     ]
    }
   ],
   "source": [
    "#printing newst weather\n",
    "newst_weather = weather_list[0]\n",
    "print('Latest Mars Weather:',newst_weather)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 1.D - Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days\n",
       "5            Temperature:    -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# url to df\n",
    "df_facts = pd.read_html(\"https://space-facts.com/mars/\")\n",
    "# df_facts\n",
    "df_facts = df_facts[0]\n",
    "df_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [],
   "source": [
    "# html table string\n",
    "mars_table = df_facts.to_html(\"mars_table.html\", index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step 1.E Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [],
   "source": [
    "# url and BS\n",
    "url_Hemi = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(url_Hemi)\n",
    "time.sleep(1)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#creating hemi image title list and pulling from site\n",
    "hemi_title_list = []\n",
    "\n",
    "for img_title in soup.find_all('div',class_=\"description\"):\n",
    "    hemi_title_list.append(img_title.find('h3').text)\n",
    "hemi_title_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov//cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png',\n",
       " 'https://astrogeology.usgs.gov//cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png',\n",
       " 'https://astrogeology.usgs.gov//cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png',\n",
       " 'https://astrogeology.usgs.gov//cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png']"
      ]
     },
     "execution_count": 200,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#creating hemi url list for images and pulling thumbnail url from site\n",
    "hemi_thumb_img_list=[]\n",
    "\n",
    "for image in soup.find_all('div', class_='item'):\n",
    "    url = \"https://astrogeology.usgs.gov/\"\n",
    "    hemi_thumb_img_list.append(url + image.find('img').get('src'))\n",
    "hemi_thumb_img_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov//cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif/full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif/full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif/full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif/full.jpg']"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#stripping thumbnail and adding full image tag\n",
    "full_img_list=[]\n",
    "for all_url in hemi_thumb_img_list:\n",
    "    split_thumb= all_url.split('.tif_thumb.png')[0]\n",
    "    full_tag = split_thumb+'.tif/full.jpg'\n",
    "    full_img_list.append(full_tag)\n",
    "full_img_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Valles Marineris Hemisphere',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif/full.jpg'},\n",
       " {'title': 'Cerberus Hemisphere',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere',\n",
       "  'img_url': 'https://astrogeology.usgs.gov//cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 216,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_hemi_info = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": full_img_list[3]},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": full_img_list[0]},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": full_img_list[1]},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": full_img_list[2]},\n",
    "]\n",
    "mars_hemi_info"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
