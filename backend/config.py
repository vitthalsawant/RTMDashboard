"""
config.py
Loads environment variables for the RTM backend application.
"""

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")