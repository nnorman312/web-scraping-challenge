{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Nasa Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the NASA Mars News Site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\"><a href=\"/news/8654/how-nasas-perseverance-mars-team-adjusted-to-work-in-the-time-of-coronavirus/\" target=\"_self\">How NASA's Perseverance Mars Team Adjusted to Work in the Time of Coronavirus </a></div>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Parse Results HTML with BeautifulSoup\n",
    "html = browser.html\n",
    "soup_setup = BeautifulSoup(html, \"html.parser\")\n",
    "slide_setup = soup_setup.select_one(\"ul.item_list li.slide\")\n",
    "slide_setup.find(\"div\", class_=\"content_title\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How NASA's Perseverance Mars Team Adjusted to Work in the Time of Coronavirus \n"
     ]
    }
   ],
   "source": [
    "# Scrape the Latest News Title\n",
    "news_title = slide_setup.find(\"div\", class_=\"content_title\").get_text()\n",
    "print(news_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Like much of the rest of the world, the Mars rover team is pushing forward with its mission-critical work while putting the health and safety of their colleagues and community first.\n"
     ]
    }
   ],
   "source": [
    "# Scrape the Latest Paragraph Text\n",
    "news_p = slide_setup.find(\"div\", class_=\"article_teaser_body\").get_text()\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the url for JPL Featured Space Image\n",
    "nasa_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(nasa_images_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Click on Full (Featured Space) Image \n",
    "full_image_path = browser.find_by_id(\"full_image\")\n",
    "full_image_path.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Click on 'More Info'\n",
    "browser.is_element_present_by_text(\"more info\", wait_time=1)\n",
    "more_info_element = browser.links.find_by_partial_text(\"more info\")\n",
    "more_info_element.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse Results HTML with BeautifulSoup\n",
    "html = browser.html\n",
    "image_soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA16225_hires.jpg'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get Full JPG Featured Space Image Path \n",
    "featured_image_url = image_soup.select_one(\"figure.lede a img\").get(\"src\")\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "# Create HTML for Full JPG Featured Space Image\n",
    "featured_image_url = f\"https://www.jpl.nasa.gov{featured_image_url}\"\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Mars Weather Twitter Account\n",
    "mars_weather_url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(mars_weather_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse Results HTML with BeautifulSoup\n",
    "html = browser.html\n",
    "mars_weather_soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Facts "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
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
       "      <th>Values</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parameter</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                             Values\n",
       "Parameter                                          \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the Mars Facts Site and Use Pandas to Scrape the Table Containing Facts about the Planet\n",
    "mars_facts = pd.read_html(\"https://space-facts.com/mars/\")[0]\n",
    "mars_facts.columns = [\"Parameter\", \"Values\"]\n",
    "mars_facts.set_index([\"Parameter\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Parameter</th>\\n      <th>Values</th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>0</th>\\n      <td>Equatorial Diameter:</td>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>1</th>\\n      <td>Polar Diameter:</td>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>2</th>\\n      <td>Mass:</td>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>3</th>\\n      <td>Moons:</td>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>4</th>\\n      <td>Orbit Distance:</td>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>5</th>\\n      <td>Orbit Period:</td>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>6</th>\\n      <td>Surface Temperature:</td>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>7</th>\\n      <td>First Record:</td>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>8</th>\\n      <td>Recorded By:</td>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use Pandas to Convert the Data to a HTML Table String\n",
    "html_table = mars_facts.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Parameter</th>      <th>Values</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <th>1</th>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <th>2</th>      <td>Mass:</td>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <th>3</th>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>4</th>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <th>5</th>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>6</th>      <td>Surface Temperature:</td>      <td>-87 to -5 °C</td>    </tr>    <tr>      <th>7</th>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>8</th>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Replace values\n",
    "html_table = html_table.replace(\"\\n\", \"\")\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up Chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the USGS Site\n",
    "usgs_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(usgs_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Click Each of the Links to the Hemispheres in Order to Find the Image URL to the Full Image\n",
    "\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# Get a List of All the Hemispheres\n",
    "links = browser.find_by_css(\"a.product-item h3\")\n",
    "for item in range(len(links)):\n",
    "    hemisphere = {}\n",
    "    \n",
    "    # Find Element on Each Loop to Avoid a Stale Element Exception\n",
    "    browser.find_by_css(\"a.product-item h3\")[item].click()\n",
    "    \n",
    "    # Find Sample Image and Extract <href>\n",
    "    sample_element = browser.find_link_by_text(\"Sample\").first\n",
    "    hemisphere[\"img_url\"] = sample_element[\"href\"]\n",
    "    \n",
    "    # Get Hemisphere Title\n",
    "    hemisphere[\"title\"] = browser.find_by_css(\"h2.title\").text\n",
    "    \n",
    "    # Append Hemisphere Object to List\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "    \n",
    "    # Navigate Backwards\n",
    "    browser.back()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print Image URLs\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
