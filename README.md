Mission to Mars

In this assignment, I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

The web scraping entails the following:
- Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text
- Visit the url for JPL Featured Space Image and use splinter to navigate the site and find the image url for the current Featured Mars Image 
- Visit the Mars Weather Twitter account and scrape the latest Mars weather tweet from the page
- Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, and more.
- Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres

Once I successfully complete these tasks, I use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped. The template HTML file called index.html herein takes the Mars data dictionary and displays all of the data in the appropriate HTML elements. See the Webpage Result file for a quick preview.
