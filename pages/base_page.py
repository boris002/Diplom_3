import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть по элементу: {locator}")
    def click_button(self, locator, timeout=10):
        try:
            element = self.wait_element_clickable(locator, timeout)
            element.click()
        except Exception:
            element = self.wait_element_visible(locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидание кликабельного элемента: {locator}")
    def wait_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание видимого элемента: {locator}")
    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Заполнить поле текстом: {locator}")
    def fill_field(self, locator, text):
        field = self.wait_element_visible(locator)
        field.clear()
        field.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        element = self.wait_element_visible(locator)
        return element.text.strip()

    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    @allure.step("Проверить невидимость элемента: {locator}")
    def is_not_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return not element.is_displayed()
        except:
            return True

    @allure.step("Драг-н-дроп элемента")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_element_visible(source_locator)
        target = self.wait_element_visible(target_locator)
        js_code = """
            function triggerDragAndDrop(sourceNode, destinationNode) {
                const dataTransfer = new DataTransfer();
                sourceNode.dispatchEvent(new DragEvent('dragstart', { bubbles: true, dataTransfer }));
                destinationNode.dispatchEvent(new DragEvent('drop', { bubbles: true, dataTransfer }));
                sourceNode.dispatchEvent(new DragEvent('dragend', { bubbles: true, dataTransfer }));
            }
            triggerDragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_code, source, target)

    @allure.step("Ждать выполнения условия")
    def wait_until(self, condition_func, timeout=15, poll_frequency=0.5):
        end_time = time.time() + timeout
        while time.time() < end_time:
            if condition_func():
                return True
            time.sleep(poll_frequency)
        raise Exception("Условие не выполнено за отведённое время")
    @allure.step("Найти все элементы по локатору: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

