import allure
import pytest
from data import INGREDIENT_NAMES
from pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver


class TestMainPage:
    @allure.title('Можно перейти в Конструктор бургера кликом на кнопку "Конструктор"')
    def test_click_constructor_btn(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.go_to_order_feed_page()
        main_page.click_constructor_header()
        
        assert main_page.is_main_page_opened()

    @allure.title('Можно перейти в Ленту Заказов по клику на кнопку "Лента Заказов"')
    def test_click_orders_btn(self, driver: WebDriver) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_order_feed_header()
        
        assert main_page.is_order_feed_opened()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize('ingredient_name', INGREDIENT_NAMES)
    def test_click_ingredient(self, driver: WebDriver, ingredient_name: str) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(ingredient_name)
        
        assert main_page.ingredient_details_is_displayed()

    @allure.title('Можно закрыть модалку об ингредиенте кликом на кнопку крестика')
    @pytest.mark.parametrize('ingredient_name', INGREDIENT_NAMES)
    def test_click_close_ingredient_details(self, driver: WebDriver, ingredient_name: str) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        main_page.click_on_ingredient(ingredient_name)
        main_page.click_close_details_button()
        
        assert main_page.ingredient_details_is_displayed() is False

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @pytest.mark.parametrize('ingredient_name', INGREDIENT_NAMES)
    def test_add_ingredient_counter_changed(self, driver: WebDriver, ingredient_name: str) -> None:
        main_page = MainPage(driver)
        main_page.go_to_main_page()
        count_before = main_page.get_ingredient_count(ingredient_name)
        main_page.move_ingredient_to_basket(ingredient_name)
        
        assert main_page.get_ingredient_count(ingredient_name) > count_before

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order_authorized_user(self, login: WebDriver) -> None:
        main_page = MainPage(login)
        main_page.move_ingredient_to_basket(INGREDIENT_NAMES[0])
        main_page.click_order_button()
        
        assert main_page.is_order_accepted()
