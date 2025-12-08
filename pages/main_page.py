import allure
from pages.base_page import BasePage
from locators.main_locators import *
from data.urls import BASE_URL


class MainPage(BasePage):
    URL = BASE_URL

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(self.URL)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click_button(BUTTON_CONSTRUCTOR)

    @allure.step("Перейти во вкладку 'Лента заказов'")
    def go_to_feed(self):
        self.click_button(BUTTON_FEED, timeout=25)
        self.wait_until(lambda: self.is_visible(TEXT_FEED_HEADER), timeout=10)

    @allure.step("Перетащить первый ингредиент в конструктор")
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(FIRST_INGREDIENT_IMAGE, CONSTRUCTOR_DROP_AREA)

    @allure.step("Создать заказ")
    def create_order(self):
        self.drag_ingredient_to_constructor()
        self.wait_until(lambda: self.is_visible(BUTTON_PLACE_ORDER))
        self.click_button(BUTTON_PLACE_ORDER)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        # Ждём, когда временный номер исчезнет
        try:
            self.wait_for_element_to_disappear(ORDER_NUMBER_LOADING, timeout=30)
        except Exception:
            pass  

        # Ждём появления реального номера
        element = self.wait_for_element_to_appear(ORDER_NUMBER_MODAL, timeout=30)
        return int(element.text.strip())
    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        order_number = self.get_order_number()
        self.close_modal_if_visible(ORDER_NUMBER_MODAL, BUTTON_CLOSE_ORDER_MODAL)
        return order_number

    #Логин
    @allure.step("Клик по кнопке 'Войти' на главной странице")
    def click_login_main(self):
        self.click_button(BUTTON_LOGIN_MAIN)

    @allure.step("Авторизация пользователя с email")
    def login(self, email="Boris@example.ru", password="test@123"):
        self.click_login_main()
        self.fill_field(INPUT_LOGIN_EMAIL, email)
        self.fill_field(INPUT_LOGIN_PASSWORD, password)
        self.click_button(BUTTON_LOGIN)
        self.wait_until(lambda: self.is_visible(BUTTON_PLACE_ORDER), timeout=25)

    @allure.step("Открыть модалку первого ингредиента")
    def click_ingredient(self):
        self.click_button(FIRST_INGREDIENT_CARD)
        self.wait_until(lambda: self.is_visible(MODAL_INGREDIENT_DETAILS))

    @allure.step("Закрыть модалку ингредиента")
    def close_ingredient_modal(self):
        self.close_modal_if_visible(MODAL_INGREDIENT_DETAILS, BUTTON_CLOSE_MODAL)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        if self.is_visible(COUNTER_INGREDIENT):
            return int(self.get_text(COUNTER_INGREDIENT))
        return 0

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def modal_visible(self):
        return self.is_visible(MODAL_INGREDIENT_DETAILS)

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def modal_closed(self):
        return self.is_not_visible(MODAL_INGREDIENT_DETAILS)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получить значение счётчика ингредиента после увеличения")
    def get_ingredient_counter_increased(self, previous_value):
        self.wait_until(lambda: self.get_ingredient_counter() > previous_value)
        return self.get_ingredient_counter()
