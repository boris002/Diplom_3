import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.epic("Лента заказов")
class TestFeedCounters:

    @allure.title("Создание заказа увеличивает счётчик 'Выполнено за всё время'")
    def test_total_orders_counter_increases(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main_page()
        main.login()
        main.go_to_feed() 

        total_before = feed.get_total_orders()

        main.click_constructor()
        main.create_order()
        order_number = main.close_order_modal()

        main.go_to_feed()
        main.wait_until(lambda: feed.get_total_orders() > total_before, timeout=20)
        total_after = feed.get_total_orders()

        assert total_after > total_before, "Счётчик 'Выполнено за всё время' не увеличился"

    @allure.title("Создание заказа увеличивает счётчик 'Выполнено за сегодня'")
    def test_today_orders_counter_increases(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)

        main.open_main_page()
        main.login()
        main.go_to_feed()
        today_before = feed.get_total_today()

        main.click_constructor()
        main.create_order()
        order_number = main.close_order_modal()

        main.go_to_feed()
        main.wait_until(lambda: feed.get_total_today() > today_before, timeout=20)
        today_after = feed.get_total_today()

        assert today_after > today_before, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)

        main.open_main_page()
        main.login()
        main.click_constructor()
        main.create_order()
        order_number = main.close_order_modal()

        main.go_to_feed()
        feed.wait_until_feed_loaded()  

        feed.wait_for_order_in_progress(order_number, timeout=30)
        assert feed.is_order_in_progress(order_number), (
            f"Заказ {order_number} не найден в разделе 'В работе'"
        )
