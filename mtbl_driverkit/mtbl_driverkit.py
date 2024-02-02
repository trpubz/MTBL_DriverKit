# MTBLDriverKit.py
# by pubins.taylor
# created 10 MAY 22
# edited 1 FEB 24
# v0.3.2
# Houses the generics for Selenium WebDriver for multiple uses
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def dk_driver_config(invoking_module_path: os.path, headless=True) -> tuple[webdriver.Chrome, str]:
    """
    Handles webdriver config management by passing the desired options as arguments.
    :param invoking_module_path: type os.path (string).  The driver will download files,
    like a .csv, to this directory.
    :param headless: boolean.  Indicates whether to draw the webdriver window.
    :return: selenium.webdriver.chrome, download directory string
    """
    options = webdriver.ChromeOptions()

    project_root = find_root_directory(invoking_module_path)
    temp_download_dir = os.path.join(project_root, "temp/")

    prefs = {"download.default_directory": temp_download_dir}
    options.add_experimental_option("prefs", prefs)
    options.page_load_strategy = "none"
    if headless:
        options.add_argument("--headless")
    # ChromeDriverManager().install() downloads latest version of chrome driver to avoid
    # compatibility issues
    driver = webdriver.Chrome(options=options, service=ChromeService())

    return driver, temp_download_dir


def find_root_directory(start_path: os.path) -> os.path:
    """
    find the root dir of the project
    """
    current_path = start_path
    while not os.path.exists(os.path.join(current_path, 'app/')):
        parent_path = os.path.dirname(current_path)

        if parent_path == current_path:
            raise FileNotFoundError("app/ not found in any parent directory")

        current_path = parent_path

    return current_path
