import os

class Config:
    SECRET_KEY = '6a5b826c18f5db76e78adf63ecd0af76'
    

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}