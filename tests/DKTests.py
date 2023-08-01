import unittest
import os
from DriverKit import DriverKit
import selenium

class TestDKConfigs(unittest.TestCase):


    def test_open_nonheadless(self):
        test_driver: selenium.webdriver = DriverKit.DKDriverConfig(headless=False)
        test_driver.get("http://www.google.com")
        assert test_driver.title == "Google"
        test_driver.quit()

    def test_download_dir(self):
        driver_dir = DriverKit.DKDirBuilder()
        os.makedirs(driver_dir, exist_ok=True)

        with open(os.path.join(driver_dir, "temp.py"), "w"):
            os.remove(os.path.join(driver_dir, "temp.py"))
        self.assertTrue(driver_dir.endswith("DriverKit/temp/"))


if __name__ == '__main__':
    unittest.main()
