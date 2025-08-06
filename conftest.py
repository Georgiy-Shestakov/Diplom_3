from typing import Any, Generator

import pytest
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request) -> Generator[WebDriver, Any, None]:
    driver: WebDriver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver: WebDriver) -> WebDriver:
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login()
    return driver
