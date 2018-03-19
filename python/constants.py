import os

PYTHON_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_DIR = PYTHON_DIR[:PYTHON_DIR.index('python')]

# Maximum page number is 10000
MAX_PAGE_NUMBER = 100

DATA_DIR = os.path.join(PROJECT_DIR, 'data')
