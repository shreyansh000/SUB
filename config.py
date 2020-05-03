import os


class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    api_id = int(os.environ.get("api_id", None))
    api_hash = os.environ.get("api_hash", "")
    string_session = os.environ.get("string_session", "")

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True
