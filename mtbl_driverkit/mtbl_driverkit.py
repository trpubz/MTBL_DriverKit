# MTBLDriverKit.py
# by pubins.taylor
# created 10 MAY 22
# edited 28 JAN 24
# v0.3.0
# Houses the generics for Selenium WebDriver for multiple uses
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def DKDriverConfig(dirDownload: os.path = "root", headless=True) -> tuple[webdriver.Chrome, str]:
    """
    Handles webdriver config management by passing the desired options as arguments.
    :param dirDownload: type os.path (string).  The driver will download files, like a .csv, to this directory.
    :param headless: boolean.  Indicates whether to draw the webdriver window.
    :return: selenium.webdriver.chrome, download directory string
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

    return driver, downloadDir


def DKDirBuilder(dirDownload: os.path = "root") -> os.path:
    """
    Builds a directory on the user preference.
    :param dirDownload: String representation of the desired directory to download.  If nothing passed,
    defaults to the project's root directory.  The root directory is defined as the dir level with [main.py]
    :return: the os.path which is a string
    """
    outputPath: os.path

    if dirDownload == "root":
        projectRoot = find_main_py_directory(os.path.abspath(__file__))
        outputPath = os.path.join(projectRoot, "temp/")
    elif dirDownload.startswith("C:\\") or dirDownload.startswith("/Users"):
        outputPath = dirDownload
    else:
        raise NotADirectoryError()

    return outputPath


def find_main_py_directory(start_path: os.path) -> os.path:
    """
    Could be invoked by passing in os.path.abspath(__file__)
    which would find the main.py directory if this file is nested in the .venv libraries.
    """
    current_path = start_path
    while not os.path.exists(os.path.join(current_path, 'main.py')):
        parent_path = os.path.dirname(current_path)

        if parent_path == current_path:
            # Reached the root directory without finding 'main.py'
            raise FileNotFoundError("main.py not found in any parent directory")

        current_path = parent_path

    return current_path


def DKCheckDownloadsChrome(driver: webdriver.Chrome):
    driver.get("chrome://settings/?search=downloads")
    # TODO: figure out how to find 'location'
