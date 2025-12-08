import allure
from pages.main_page import MainPage


@allure.epic("Модальное окно ингредиента")
class TestIngredientModal:

    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_ingredient_modal_opens(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_ingredient()
        assert page.modal_visible(), "Модальное окно не открылось при клике на ингредиент"

    @allure.title("Модальное окно ингредиента закрывается по крестику")
    def test_ingredient_modal_closes(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_ingredient()
        page.close_ingredient_modal()
        assert page.modal_closed(), "Модальное окно не закрылось после нажатия крестика"
