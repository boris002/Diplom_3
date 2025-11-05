import allure
from pages.main_page import MainPage
from locators.main_locators import TEXT_FEED_HEADER, CONSTRUCTOR_TITLE


@allure.epic("Навигация между разделами")
class TestNavigation:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.go_to_feed()
        assert page.is_visible(TEXT_FEED_HEADER), "Не открылась лента заказов перед возвратом"

        page.click_constructor()
        assert page.is_visible(CONSTRUCTOR_TITLE), "Раздел конструктора не стал активным после клика"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_feed(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.go_to_feed()
        assert page.is_visible(TEXT_FEED_HEADER), "Не открылась лента заказов"
