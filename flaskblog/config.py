import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://mgzvqwvsdfedlv:c7b6bad0ab89b5a6b6464d21f8259b48fdbeed5ba8a6f5379bc232b936f71fef@ec2-54-224-124-241.compute-1.amazonaws.com:5432/d8paa7bkcbgk69'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'noreply.nihalblog@gmail.com'
    MAIL_PASSWORD = 'Nihalpuram007'