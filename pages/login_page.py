import allure
from data import Urls, User
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def go_to_login_page(self) -> None:
        self.driver_get_url(Urls.login_page)
        self.find_clickable_element(LoginPageLocators.login_btn)

    @allure.step('Кликаем по элементу "Восстановить пароль"')
    def click_recover_password_text(self) -> None:
        self.click_on_element(LoginPageLocators.recover_password_text_href)

    @allure.step('Заполняем поле логина')
    def fillup_login(self, login_data: str) -> None:
        self.send_keys_into_field(LoginPageLocators.email_fld, login_data)

    @allure.step('Заполняем поле пароля')
    def fillup_password(self, password: str) -> None:
        self.send_keys_into_field(LoginPageLocators.password_fld, password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login_button(self) -> None:
        self.click_on_element(LoginPageLocators.login_btn)

    @allure.step('Выполняем авторизацию пользователя')
    def login(self):
        self.find_visible_element(LoginPageLocators.title)
        self.fillup_login(User.login)
        self.fillup_password(User.password)
        self.click_login_button()
        self.wait_element_to_be_invisible(LoginPageLocators.login_btn)

    def is_login_page_opened(self) -> bool:
        return (self.current_url() == Urls.login_page and self.find_visible_element(LoginPageLocators.login_btn) is not None)
