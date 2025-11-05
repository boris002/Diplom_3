from selenium.webdriver.common.by import By

# Главная страница
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
TEXT_CONSTRUCTOR_PAGE = (By.XPATH, "//button[text()='Оформить заказ']")
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
BUTTON_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
TEXT_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

TAB_BUNS = (By.XPATH, "//span[text()='Булки']/parent::div")
TEXT_BUNS = (By.XPATH, "//h2[text()='Булки']")
TAB_SAUCES = (By.XPATH, "//span[text()='Соусы']/parent::div")
TEXT_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
TAB_FILLINGS = (By.XPATH, "//span[text()='Начинки']/parent::div")
TEXT_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")

#Модальное окно ингредиента
FIRST_INGREDIENT_CARD = (By.XPATH, "(//div[contains(@class,'BurgerIngredient_ingredient__')])[1]")
MODAL_INGREDIENT_DETAILS = (By.XPATH, "//section[contains(@class,'Modal_modal_opened__')]")
BUTTON_CLOSE_MODAL = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

# Счётчики ингредиентов
COUNTER_INGREDIENT = (By.XPATH, "(//p[contains(@class,'counter_counter__')])[1]")
BUTTON_ADD_INGREDIENT = (By.XPATH, "(//button[contains(@class,'button_button__')])[1]")

#Оформление заказа
BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
ORDER_NUMBER = (By.XPATH, "//h2[contains(text(),'номер заказа')]")

#Раздел "Лента заказов"
# Общие счётчики
BLOCK_TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")

# Счётчик "Выполнено за сегодня"
BLOCK_TOTAL_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number__')]")
# Заказы, находящиеся "в работе"
BLOCK_IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul[1]/li")
BLOCK_READY = (By.XPATH, "//p[text()='Готовы:']/following-sibling::ul[1]/li")

# Каждый заказ в ленте (его номер)
ORDER_NUMBER_FEED = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__')]")

# Страница регистрации 
INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
INPUT_PASSWORD = (By.XPATH, "//input[@type='password' and @name='Пароль']")
BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")
LINK_REGISTER_TO_LOGIN = (By.XPATH, "//a[text()='Войти']")
TEXT_REGISTRATION_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")

# Страница авторизации 
INPUT_LOGIN_EMAIL = (By.XPATH, "//input[@name='name']")
INPUT_LOGIN_PASSWORD = (By.XPATH, "//input[@type='password']")
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
TEXT_LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
BLOCK_LOGIN_FORM = (By.XPATH, "//div[@class='Auth_login__3hAey']")
LINK_LOGIN_TO_REGISTER = (By.XPATH, "//a[@href='/register' and contains(@class,'Auth_link')]")

# Восстановление пароля
LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
TEXT_RECOVER_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
LINK_RECOVER_TO_LOGIN = (By.XPATH, "//a[text()='Войти']")

#переход по логотипу 
LOGO_STELLAR = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a")

# Личный кабинет
BLOCK_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@class,'Account_link_active')]")


# область конструктора
CONSTRUCTOR_DROP_AREA = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")

# изображение первого ингредиента
FIRST_INGREDIENT_IMAGE = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient__')]//img)[1]")
# Номер заказа в модалке после оформления
ORDER_NUMBER_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and not(text()='9999')]")
ORDER_NUMBER_LOADING = (By.XPATH, "//h2[text()='9999']")
BUTTON_CLOSE_ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__')]//button[contains(@class,'close')]")
