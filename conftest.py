import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
