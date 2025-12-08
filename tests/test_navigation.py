import allure
from pages.main_page import MainPage
from locators.main_locators import TEXT_FEED_HEADER, CONSTRUCTOR_TITLE
from data.urls import BASE_URL

@allure.epic("Навигация между разделами")
class TestNavigation:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_constructor()
        #Проверить, что текущий URL соответствует главной странице
        current_url = page.get_current_url()
        assert current_url == BASE_URL, f"Ожидался URL {BASE_URL}, но получили {current_url}"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_feed(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.go_to_feed()
        assert page.is_visible(TEXT_FEED_HEADER), "Не открылась лента заказов"
