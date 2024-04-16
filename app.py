# Import Flask framework and other necessary modules
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import config

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage ("/") that handles both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":  # If the request method is POST (form submitted)
        query = request.form.get("query")  # Get the search query from the form
        if query:  # If query is not empty, fetch news based on the query
            articles = fetch_news(query)
        else:  # If query is empty, fetch top news
            articles = fetch_top_news()
    else:  # If request method is GET
        articles = fetch_top_news()  # Fetch top news
    return render_template("index.html", articles=articles)  # Render the HTML template with the articles

# Function to fetch top news articles
def fetch_top_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={config.MY_API_KEY}"  # Construct the API URL for top headlines
    response = requests.get(url)  # Make a GET request to the News API
    news_data = response.json()  # Parse the JSON response
    articles = news_data['articles']  # Extract the articles from the response
    return articles  # Return the list of articles

# Function to fetch news articles based on the search query
def fetch_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={config.MY_API_KEY}"  # Construct the API URL
    response = requests.get(url)  # Make a GET request to the News API
    news_data = response.json()  # Parse the JSON response
    articles = news_data['articles']  # Extract the articles from the response
    return articles  # Return the list of articles

# Entry point for running the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask development server with debugging enabled
