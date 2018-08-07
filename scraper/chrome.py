import os
import subprocess
import re
import atexit
import time

from selenium import webdriver

'''
requires the selenium python package
'''


def get_selenium_driver():
    return webdriver.Remote(
        'http://selenium:4444/wd/hub',
        webdriver.DesiredCapabilities.CHROME.copy()
    )
