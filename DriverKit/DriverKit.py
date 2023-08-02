# DriverKit.py
# by pubins.taylor
# created 10MAY22
# edited 02AUG23
# v0.1.1
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

    :note: this will only return a root directory if the module is ran from a subdirectory of the project's root directory and/or a virtual machine inside the project.
    """

    outputPath: os.path

    if dirDownload == "root":
        projectRoot = find_main_py_directory(os.path.abspath(__file__))
        outputPath = projectRoot + "/temp/"
    elif dirDownload.startswith("C:\\") or dirDownload.startswith("/Users"):
        outputPath = dirDownload
    else:
        raise NotADirectoryError()

    return outputPath


def find_main_py_directory(start_path: os.path) -> os.path:
    current_path = start_path
    while True:
        if os.path.exists(os.path.join(current_path, 'main.py')):
            return current_path
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            # Reached the root directory without finding 'main.py'
            raise FileNotFoundError("main.py not found in any parent directory")
        current_path = parent_path


def DKCheckDownloadsChrome(driver: webdriver.Chrome):
    driver.get("chrome://settings/?search=downloads")
    # TODO: figure out how to find 'location'
