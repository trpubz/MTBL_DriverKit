import pytest
import os
from mtbl_driverkit import mtbl_driverkit as DK


class TestDKConfigs:
    driver = None
    download_dir = ""

    @pytest.fixture
    def setup_and_teardown(self):
        # Setup code here
        test_driver, download_dir = DK.dk_driver_config(
            os.getcwd(),
            headless=False)
        self.driver = test_driver
        self.download_dir = download_dir

        yield
        # Teardown code here
        self.driver.quit()

    def test_open_non_headless(self, setup_and_teardown):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

    def test_open_headless(self):
        test_driver, _ = DK.dk_driver_config(os.getcwd())  # headless=True
        test_driver.get("https://www.google.com")
        assert test_driver.title == "Google"
        test_driver.quit()

    def test_download_dir(self, setup_and_teardown):
        root_dir = self.download_dir
        os.makedirs(root_dir, exist_ok=True)

        with open(os.path.join(root_dir, "temp.py"), "w"):
            os.remove(os.path.join(root_dir, "temp.py"))
        assert root_dir.endswith("/temp/")

    def test_find_main_py_directory_with_bad_start_path(self):
        with pytest.raises(FileNotFoundError):
            _ = DK.find_root_directory("/tmp")
