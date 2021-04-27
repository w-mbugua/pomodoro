import os

class Config:
    SECRET_KEY =  '79537d00f4834892986f09a100aa1edf'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig, 
}