#COPIED

import configparser
import os

def createConfig(path = "Settings.ini"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.add_section("Defaults")
    config.set("Settings", "Language", "en")
    config.set("Settings", "DidBackground", "True")
    with open(path, 'w') as configFile:
        config.write(configFile)

def readConfig(path = "Settings.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    return config

def ifSettingsNotExists():
    if not os.path.exists("Settings.ini"):
        createConfig()
