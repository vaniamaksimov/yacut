import os
from string import ascii_letters, digits

from dotenv import load_dotenv

load_dotenv()

LETTERS = ascii_letters + digits
MIN_LENGTH = 1
MAX_LENGTH = 6


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
