# Configuration file

import os

API_URL = os.getenv('API_URL', 'https://default-api.com')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
