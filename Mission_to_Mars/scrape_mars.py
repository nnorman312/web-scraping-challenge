# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
from selenium import webdriver

# Initialize Splinter Browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# Setup Scrape
def scrape():
    # Setup Empty Dictionary to Store Mars Info
    mars_info = {}


    # Mars News
    # Visit the NASA Mars News Site
    browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
   
    # Parse Results HTML with BeautifulSoup
    soup_setup = BeautifulSoup(html, "html.parser")
    slide_setup = soup_setup.select_one("ul.item_list li.slide")
    slide_setup.find("div", class_="content_title")

    # Scrape the Latest News Title
    news_title = slide_setup.find("div", class_="content_title").get_text()

    # Scrape the Latest Paragraph Text
    news_p = slide_setup.find("div", class_="article_teaser_body").get_text()

    # Add Results to Mars Info Dictionary
    mars_info["news_title"] = news_title
    mars_info["teaser"] = news_p


    # JPL Mars Space Images - Featured Image
    # Visit the url for JPL Featured Space Image
    nasa_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(nasa_images_url)

    # Click on Full (Featured Space) Image 
    full_image_path = browser.find_by_id("full_image")
    full_image_path.click()

    # Click on 'More Info'
    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_element = browser.links.find_by_partial_text("more info")
    more_info_element.click()

    # Parse Results HTML with BeautifulSoup
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")

    # Get Full JPG Featured Space Image Path 
    featured_image_url = image_soup.select_one("figure.lede a img").get("src")

    # Create HTML for Full JPG Featured Space Image
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image_url}"

    # Add Results to Mars Info Dictionary
    mars_info["featured_image_url"] = featured_image_url


    # Mars Weather
    # Visit the Mars Weather Twitter Account
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)
    
    # Parse Results HTML with BeautifulSoup
    html = browser.html
    mars_weather_soup = BeautifulSoup(html, "html.parser")
    
    # Scrape Twitter Account for Latest Tweet
    mars_weather = mars_weather_soup.find("p", class_="tweet-text").text
    print(mars_weather)

    # Add Result to Mars Info Dictionary
    mars_info["mars_weather"] = mars_weather


    # Mars Facts
    # Visit the Mars Facts Site and Use Pandas to Scrape the Table Containing Facts about the Planet
    mars_facts = pd.read_html("https://space-facts.com/mars/")[0]
    mars_facts.columns = ["Parameter", "Values"]
    mars_facts.set_index(["Parameter"])

    # Use Pandas to Convert the Data to a HTML Table String
    html_table = mars_facts.to_html()

    # Replace values
    html_table = html_table.replace("\n", "")

    # Add Results to Mars Info Dictionary
    mars_info["mars_table"] = html_table


    # Mars Hemisphere
    # Visit the USGS Site
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)

    # Click Each of the Links to the Hemispheres in Order to Find the Image URL to the Full Image
    hemisphere_image_urls = []

    # Get a List of All the Hemispheres
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        hemisphere = {}
    
        # Find Element on Each Loop to Avoid a Stale Element Exception
        browser.find_by_css("a.product-item h3")[item].click()
    
        # Find Sample Image and Extract <href>
        sample_element = browser.links.find_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
    
        # Get Hemisphere Title
        hemisphere["title"] = browser.find_by_css("h2.title").text
    
        # Append Hemisphere Object to List
        hemisphere_image_urls.append(hemisphere)
    
        # Navigate Backwards
        browser.back()

        # Add Results to Mars Info Dictionary
        mars_info["hemispheres"] = hemisphere_image_urls

    # Quit browser
    browser.quit()

    return mars_info
