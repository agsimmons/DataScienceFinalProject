import sqlalchemy

USERNAME = 'andrew'
HOST = 'localhost'
DATABASE = 'smart'


def get_engine():
    return sqlalchemy.create_engine(f'postgresql://{USERNAME}@/{DATABASE}')
