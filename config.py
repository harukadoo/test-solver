import os
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("UNIVERSITY_LOGIN")
PASSWORD = os.getenv("UNIVERSITY_PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL")

if not LOGIN or not PASSWORD or not LOGIN_URL:
    raise ValueError("error: not all variables are filled in the .env file")