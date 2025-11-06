import allure
from pages.base_page import BasePage
from locators.main_locators import *

class FeedPage(BasePage):

    @allure.step("Ожидание загрузки ленты заказов")
    def wait_until_feed_loaded(self, timeout=25):
        self.wait_element_visible(BLOCK_TOTAL_ORDERS, timeout)
    
    @allure.step("Проверка наличия заказа в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        elements = self.find_elements(BLOCK_IN_PROGRESS)
        for el in elements:
            try:
                if str(order_number) in el.text:
                    return True
            except Exception:
                continue  
        return False

    @allure.step("Ожидание появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=30):
        self.wait_until(lambda: self.is_order_in_progress(order_number), timeout=timeout)

    @allure.step("Получить общее количество заказов за всё время")
    def get_total_orders(self):
        self.wait_until_feed_loaded()
        return int(self.get_text(BLOCK_TOTAL_ORDERS))

    @allure.step("Получить количество заказов, выполненных сегодня")
    def get_total_today(self):
        self.wait_until(
            lambda: self.is_visible(BLOCK_TOTAL_TODAY) and self.get_text(BLOCK_TOTAL_TODAY).isdigit(),
            timeout=25
        )
        return int(self.get_text(BLOCK_TOTAL_TODAY))
    @allure.step("Получить общее количество заказов за всё время после обновления")
    def get_total_orders_increased(self, previous_value):
        self.wait_until(lambda: self.get_total_orders() > previous_value, timeout=20)
        return self.get_total_orders()
    @allure.step("Получить количество заказов, выполненных сегодня после обновления")
    def get_total_today_increased(self, previous_value):
        self.wait_until(lambda: self.get_total_today() > previous_value, timeout=20)
        return self.get_total_today()

