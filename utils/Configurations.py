import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('resources/properties.ini')
    return config


def get_token():
    # return os.getenv("GIT_API_TOKEN")
    return get_config()["API"]["token"]


def get_user():
    # return os.getenv("GIT_API_TOKEN")
    return get_config()["API"]["git_user"]


def get_invalid_token():
    return get_config()["API"]["invalid_token"]
