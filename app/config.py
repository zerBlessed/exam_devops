import os

SECRET_KEY = '123456qwerty'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://std_2059_test_exam:12345678@std-mysql.ist.mospolytech.ru/std_2059_test_exam'
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:secret@mysql_db/cinema'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = False

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')