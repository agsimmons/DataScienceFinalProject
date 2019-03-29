import pathlib

PROJECT_DIR = pathlib.Path(__file__).parent

DATA_DIR = PROJECT_DIR / pathlib.Path('data')

DATA_DB = PROJECT_DIR / 'data.sqlite3'
