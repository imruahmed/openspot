import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'development key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

UW_API_KEY = '73d6652b8f8866a68b4129fd92d83ab8'

# email server
MAIL_SERVER = 'smtp.mail.yahoo.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'imranahmed_uw20@yahoo.ca'
MAIL_PASSWORD = 'ilikechicken123!'

# administrator list
ADMINS = ['imranahmed_uw20@yahoo.ca']

CURRENT_TERM = '1161'
COURSE_LIST = ['ACC', 'ACINTY', 'ACTSC', 'ADMGT', 'AFM', 'AHS', 'AMATH', 'ANTH', 'APPLS', 'ARBUS', 'ARCH', 'ARCHL', 'ARTS', 'AVIA', 'BASE', 'BE', 'BET', 'BIOL', 'BME', 'BUS', 'CHE', 'CHEM', 'CHINA', 'CIVE', 'CLAS', 'CM', 'CMW', 'CO', 'COGSCI', 'COMM', 'COMST', 'COOP', 'CROAT', 'CS', 'CT', 'DAC', 'DEI', 'DM', 'DRAMA', 'DUTCH', 'EARTH', 'EASIA', 'ECE', 'ECON', 'EFAS', 'EMLS', 'ENBUS', 'ENGL', 'ENVE', 'ENVS', 'ERS', 'ESL', 'EVSY', 'FINE', 'FR', 'GBDA', 'GEMCC', 'GENE', 'GEOE', 'GEOG', 'GER', 'GERON', 'GGOV', 'GLOBAL', 'GRK', 'GS', 'HIST', 'HLTH', 'HRM', 'HSG', 'HUMSC', 'INDEV', 'INTEG', 'INTST', 'INTTS', 'IS', 'ISS', 'ITAL', 'ITALST', 'JAPAN', 'JS', 'KIN', 'KOREA', 'LAT', 'LED', 'LS', 'MATBUS', 'MATH', 'ME', 'MEDVL', 'MI', 'MNS', 'MSCI', 'MTE', 'MTHEL', 'MUSIC', 'NANO', 'NATST', 'NE', 'NES', 'OPTOM', 'PACS', 'PD', 'PDARCH', 'PDENG', 'PDPHRM', 'PHARM', 'PHIL', 'PHS', 'PHYS', 'PLAN', 'PMATH', 'POLSH', 'PORT', 'PS', 'PSCI', 'PSYCH', 'QIC', 'REC', 'REES', 'RELC', 'RS', 'RUSS', 'SCBUS', 'SCI', 'SDS', 'SE', 'SI', 'SMF', 'SOC', 'SOCIN', 'SOCWK', 'SPAN', 'SPCOM', 'SPD', 'STAT', 'STV', 'SUSM', 'SWK', 'SWREN', 'SYDE', 'TAX', 'TN', 'TOUR', 'TS', 'UN', 'UNIV', 'VCULT', 'WATER', 'WKRPT', 'WS']