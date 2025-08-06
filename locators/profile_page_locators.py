from selenium.webdriver.common.by import By


class ProfilePageLocators:
    history_link_text = (By.XPATH, './/a[text()="История заказов"]')
    logout_btn = (By.XPATH, './/button[text()="Выход"]')
    order_history_div = (By.XPATH, './/div[contains(@class,"orderHistory")]')
    orders_id_list = (By.XPATH, '//div[contains(@class,"OrderHistory_textBox")]/p[contains(@class,"text_type_digits")]')
