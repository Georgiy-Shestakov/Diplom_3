import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from selenium.webdriver.remote.webdriver import WebDriver


class TestProfilePage:
    @allure.title('Авторизованный пользователь может попасть по клику в Личный кабинет')
    def test_click_profile_authorized_user(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        main_page.click_profile_text()
        
        assert ProfilePage(login).is_profile_page_opened()

    @allure.title('Можно перейти в Историю заказов из Личного кабинета')
    def test_click_history_btn(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        main_page.click_profile_text()
        profile_page.click_order_history()
        
        assert profile_page.is_order_history_opened()

    @allure.title('Можно выйти из аккаунта кликом по кнопке "Выйти" в Личном кабинете')
    def test_click_logout_btn(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        main_page.click_profile_text()
        profile_page.click_logout_button()
        profile_page.wait_change_profile_page_after_logout()
        
        assert LoginPage(login).is_login_page_opened()
