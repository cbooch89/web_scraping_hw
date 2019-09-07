from flask import Flask, render_template, redirect, jsonify
from  flask_pymongo import PyMongo
import scrape_mars

# Use flask_pymongo to set up mongo connection
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# route
@app.route("/")
def index():
    mars_info = mongo.db.collection.find_one()

    print(mars_info)

    return render_template("index.html", mars = mars_info)

@app.route("/scrape")
def scrape():
    
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)