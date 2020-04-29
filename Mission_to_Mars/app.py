# Setup and Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create instance of flask app
app = Flask(__name__)

# Establish Mongo Connection
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_info"
mongo = PyMongo(app)

# Create route that renders index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info = mars_info)

# Create route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_info = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_info.update({},mars_info, upsert=True)

    # Redirect home
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)