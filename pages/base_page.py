import allure
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_visible_element(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return (WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)))

    def find_presence_element(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return (WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)))

    def find_clickable_element(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        return (WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)))

    def wait_element_to_be_invisible(self, locator: tuple[str, str], timeout: int = 5) -> None:
        (WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator)))

    def find_visible_elements(self, locator: tuple[str, str], timeout: int = 10) -> list[WebElement]:
        return (WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator)))

    def click_on_element(self, locator: tuple[str, str]) -> None:
        self.wait_element_to_be_invisible(BasePageLocators.loading)
        self.find_clickable_element(locator).click()
        self.wait_element_to_be_invisible(BasePageLocators.loading)

    def send_keys_into_field(self, locator: tuple[str, str], input_value: str) -> None:
        self.find_visible_element(locator).send_keys(input_value)

    def wait_change_url(self, url_from) -> None:
        WebDriverWait(self.driver, 5).until(EC.url_changes(url_from))

    @allure.step('Открываем страницу {url}')
    def driver_get_url(self, url: str) -> None:
        self.driver.get(url)

    @allure.step('Узнать текущую страницу')
    def current_url(self) -> str:
        return self.driver.current_url
