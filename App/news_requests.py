import urllib.request,json
from app import app
from .models import news

Sources = news.Sources

api_key = app.config['API_KEY']

url = app.config['NEWS_API_BASE_URL']

def get_news(sources):
    """
    this function gets responses from the api call
    """