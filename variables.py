from dotenv import load_dotenv
import os
load_dotenv('prod.env')

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
