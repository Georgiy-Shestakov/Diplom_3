from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_list = (By.XPATH, './/*[contains(@class, "OrderHistory_link") and @href]')
    order_info = (By.XPATH, './/div[contains(@class, "orderBox")]/p[text()="Cостав"]')
    orders_id_list = (By.XPATH, '//div[contains(@class,"OrderHistory_textBox")]/p[contains(@class,"text_type_digits")]')
    all_time_orders_count = (By.XPATH, './/p[text()="Выполнено за все время:"]/../p[contains(@class,"OrderFeed_number")]')
    today_order_count = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/../p[contains(@class,"OrderFeed_number")]')
    orders_in_work_list = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li[contains(@class,"text_type_digits-default")]')
