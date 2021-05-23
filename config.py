import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'l1\xb0\x1dt;t1EG8I\x07\xff$\xd2'

    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }
