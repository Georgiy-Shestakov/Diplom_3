import allure
from faker import Faker
from pages.login_page import LoginPage
from pages.password_page import PasswordPage
from selenium.webdriver.remote.webdriver import WebDriver


class TestPasswordRecovery:
    @allure.title('При нажатии на кнопку "Восстановить пароль" переход в окно восстановления парля')
    def test_click_recover_password_opens_forgot_password_page(self, driver: WebDriver) -> None:
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_recover_password_text()
        
        assert PasswordPage(driver).is_forgot_password_page_opened()

    @allure.title('При нажатии "Восстановить" переход на страницу смены пароля (с почтой)')
    def test_click_forgot_btn_opens_reset_password_page(self, driver: WebDriver) -> None:
        recover_page = PasswordPage(driver)
        recover_page.go_to_recover_password_page()
        recover_page.fillup_email(Faker().email())
        recover_page.click_recover_password_button()
        recover_page.wait_change_forgot_page()
        
        assert recover_page.is_reset_password_page_opened()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_switcher_shows_password(self, driver: WebDriver) -> None:
        recover_page = PasswordPage(driver)
        recover_page.go_to_recover_password_page()
        recover_page.fillup_email(Faker().email())
        recover_page.click_recover_password_button()
        recover_page.wait_change_forgot_page()
        recover_page.click_switch_show_password_button()
        
        assert recover_page.find_active_input().text == 'Пароль'
        
