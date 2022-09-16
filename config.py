class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
