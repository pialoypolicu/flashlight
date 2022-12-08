import os

from dotenv import load_dotenv

load_dotenv('prod.env')

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
