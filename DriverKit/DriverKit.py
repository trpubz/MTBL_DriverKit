# DriverKit.py
# by pubins.taylor
# created 10MAY22
# edited 31JUL23
# v0.1.0
# Houses the generics for Selenium WebDriver for multiple uses
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def DKDriverConfig(dirDownload: os.path = "root", headless=True) -> webdriver:
    """
    Handles webdriver config management by passing the desired options as arguments.
    :param dirDownload: type os.path (string).  The driver will download files, like a .csv, to this directory.
    :param headless: boolean.  Indicates whether to draw the webdriver window.
    :return: selenium.webdriver.chrome
    """
    options = webdriver.ChromeOptions()
    downloadDir = DKDirBuilder(dirDownload)
    prefs = {"download.default_directory": downloadDir}
    options.add_experimental_option("prefs", prefs)
    options.page_load_strategy = "none"
    if headless:
        options.add_argument("--headless")
    # ChromeDriverManager().install() downloads latest version of chrome driver to avoid compatibility issues
    driver = webdriver.Chrome(options=options, service=ChromeService())

    return driver


def DKDirBuilder(dirDownload: os.path = "root") -> os.path:
    """
    Builds a directory on the user preference.
    :param dirDownload: String representation of the desired directory to download.  If nothing passed,
    defaults to the project's root directory.
    :return: the os.path which is a string
    """

    outputPath: os.path

    if dirDownload == "root":
        projectRoot = os.path.dirname(__file__)
        outputPath = projectRoot + "/temp"
    elif dirDownload.startswith("C:\\") or dirDownload.startswith("/Users"):
        outputPath = dirDownload
    else:
        raise NotADirectoryError()

    return outputPath



