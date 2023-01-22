import os
from string import ascii_letters, digits

from dotenv import load_dotenv

load_dotenv()

LETTERS = ascii_letters + digits
MIN_LENGTH = 1
MAX_LENGTH = 6


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'a606fc83e97b0e422ed95c63b9f1e07415741dedaba70a1d77d627ea8f913f61')
