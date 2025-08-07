from selenium.webdriver.common.by import By


class LoginPageLocators:
    title = (By.XPATH, './/h2[text()="Вход"]')
    login_btn = (By.XPATH, './/button[text()="Войти"]')
    email_fld = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    password_fld = (By.XPATH, './/input[@type="password"]')
    recover_password_text_href = (By.XPATH, './/a[contains(@href, "/forgot-password")]')
