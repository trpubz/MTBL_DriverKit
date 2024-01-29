import pytest
import os
from mtbl_driverkit import mtbl_driverkit as DK
import selenium.webdriver


class TestDKConfigs:
    driver = None
    download_dir = ""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Setup code here
        test_driver, download_dir = DK.DKDriverConfig(headless=False)
        self.driver = test_driver
        self.download_dir = download_dir

        yield
        # Teardown code here
        self.driver.quit()

    def test_open_non_headless(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"

    def test_download_dir(self):
        root_dir = self.download_dir
        os.makedirs(root_dir, exist_ok=True)

        with open(os.path.join(root_dir, "temp.py"), "w"):
            os.remove(os.path.join(root_dir, "temp.py"))
        assert root_dir.endswith("/temp/")

