import os

SECRET_KEY = 'admin'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='bruno',
        senha='12345678',
        servidor='localhost',
        database='lista'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'