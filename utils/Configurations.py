import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('resources/properties.ini')
    return config


def get_password():
    return "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"
