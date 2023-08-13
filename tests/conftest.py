import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        service = Service(TestData.chrome_path)
        driver = webdriver.Chrome(service=service)
        yield
        driver.close()
