import os

class Config:
    NEWS_HIGHLIGHT_API_BASE_URL ='https://newsapi.org/v2/sources?&apiKey={}'
    NEWS_HIGHLIGHT_API_KEY = os.environ.get('NEWS_HIGHLIGHT_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TOP_HEADLINES_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: the parent class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    ENV = 'development'

config_options = {
    'development': DevConfig,
    'production': ProdConfig
} 