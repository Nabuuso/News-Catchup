import os

class Config:

    
   
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    debug=False;


class DevConfig(Config):
    debug = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}