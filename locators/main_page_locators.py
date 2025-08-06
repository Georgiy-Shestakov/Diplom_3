from selenium.webdriver.common.by import By


class MainPageLocators:
    profile_link_text = (By.XPATH, './/p[text()="Личный Кабинет"]')
    order_btn = (By.XPATH, './/button[text()="Оформить заказ"]')
    constructor_link_text = (By.XPATH, './/p[text()="Конструктор"]')
    order_feed_text = (By.XPATH, './/p[text()="Лента Заказов"]')
    ingredients_section = (By.XPATH, './/section[contains(@class,"BurgerIngredients")]')
    order_feed_div = (By.XPATH, './/div[contains(@class,"orderFeed")]')
    order_start_status = (By.XPATH, './/p[text()="Ваш заказ начали готовить"]')
    order_id = (By.XPATH, './/p[text()="идентификатор заказа"]/../h2')
    order_detail_close_btn = (By.XPATH, './/p[text()="идентификатор заказа"]/../../button[contains(@class,"close")]')


class IngredientsLocators:
    @staticmethod
    def ingredient_item(name: str) -> tuple[str, str]:
        return (By.XPATH, f'.//p[text()="{name}"]/parent::a[@draggable]')

    @staticmethod
    def ingredient_counter(name: str) -> tuple[str, str]:
        return (By.XPATH, f'.//p[text()="{name}"]/../*/p[contains(@class,"num")]')

    ingredient_details_text = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    close_details_btn = (By.XPATH, './/h2[text()="Детали ингредиента"]/../../button[contains(@class,"close")]')
    ingredient_basket = (By.XPATH, './/ul[contains(@class,"basket__list")]')
