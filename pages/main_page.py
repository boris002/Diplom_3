import allure
from pages.base_page import BasePage
from locators.main_locators import *
import time


class MainPage(BasePage):
    URL = "https://stellarburgers.education-services.ru/"

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
        timeout = time.time() + 30
        # Ждём временный номер 9999
        while time.time() < timeout:
            if self.is_visible(ORDER_NUMBER_LOADING):
                break
        # Ждём финальный номер
        while time.time() < timeout:
            if self.is_visible(ORDER_NUMBER_MODAL):
                order_number = int(self.get_text(ORDER_NUMBER_MODAL))
                return order_number
        raise Exception("Реальный номер заказа не появился за 30 секунд")

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        order_number = self.get_order_number()
        if self.is_visible(BUTTON_CLOSE_ORDER_MODAL):
            self.click_button(BUTTON_CLOSE_ORDER_MODAL)
            self.wait_until(lambda: self.is_not_visible(ORDER_NUMBER_MODAL))
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
        if self.is_visible(BUTTON_CLOSE_MODAL):
            self.click_button(BUTTON_CLOSE_MODAL)
            self.wait_until(lambda: self.is_not_visible(MODAL_INGREDIENT_DETAILS))

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
