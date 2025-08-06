import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from selenium.webdriver.remote.webdriver import WebDriver


class TestOrderPage:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_details(self, driver: WebDriver) -> None:
        page = OrderFeedPage(driver)
        page.go_to_order_feed_page()
        page.click_first_order()
        
        assert page.is_order_info_displayed()


    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_of_user_exists(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        profile_page = ProfilePage(login)
        order_feed_page = OrderFeedPage(login)
        order_id = main_page.create_order_and_get_id()
        main_page.click_profile_text()
        orders_id_from_history = profile_page.get_orders_id_list()
        orders_id_from_order_feed = order_feed_page.get_orders_id_list()
        
        assert (order_id in orders_id_from_history and
                order_id in orders_id_from_order_feed and
                set(orders_id_from_history) & set(orders_id_from_order_feed) != {})

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_order_all_order_count_increases(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        order_count_before = order_feed_page.get_all_time_orders_count()
        main_page.create_order_and_get_id()
        
        assert order_feed_page.get_all_time_orders_count() > order_count_before

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_order_today_order_count_increases(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        order_count_before = order_feed_page.get_today_orders_count()
        main_page.create_order_and_get_id()
        
        assert order_feed_page.get_today_orders_count() > order_count_before

    @allure.title('после оформления заказа его ID появляется в разделе В работе')
    def test_create_order_created_id_appears(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        order_feed_page = OrderFeedPage(login)
        order_id = main_page.create_order_and_get_id()
        orders_in_work = order_feed_page.get_orders_id_in_work_list()
        
        assert order_id in orders_in_work
