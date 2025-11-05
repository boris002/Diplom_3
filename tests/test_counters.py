import allure
from pages.main_page import MainPage


@allure.epic("Конструктор бургеров")
class TestConstructor:

    @allure.title("При перетаскивании ингредиента в конструктор счётчик увеличивается")
    def test_drag_ingredient_increases_counter(self, driver):
        page = MainPage(driver)
        page.open_main_page()

        initial = page.get_ingredient_counter()
        page.drag_ingredient_to_constructor()
        page.wait_until(lambda: page.get_ingredient_counter() > initial)
        after = page.get_ingredient_counter()

        assert after > initial, f"Счётчик не увеличился (было {initial}, стало {after})"
