# Diplom_3
## Описание
Проект содержит автоматизированные тесты веб-приложения Stellar Burgers.  
Используется паттерн Page Object для описания страниц и элементов.  
Тесты выполняются в браузерах Google Chrome и Mozilla Firefox с отчётами Allure.

## Структура тестов

### BasePage
- Методы для взаимодействия с элементами: открытие страницы, клик, ввод текста, ожидание элементов, drag-and-drop.

### MainPage
- `open_main_page` — открыть главную страницу.
- `click_constructor` — перейти в конструктор бургеров.
- `go_to_feed` — перейти в ленту заказов.
- `drag_ingredient_to_constructor` — перетащить ингредиент в конструктор.
- `create_order` — создать заказ.
- `get_order_number` — получить номер заказа.
- `close_order_modal` — закрыть модальное окно заказа.
- Методы для логина и работы с модальными окнами ингредиентов.

### FeedPage
- Методы для работы с лентой заказов:
- `wait_until_feed_loaded` — дождаться загрузки ленты.
- `is_order_in_progress` — проверить наличие заказа в «В работе».
- `wait_for_order_in_progress` — дождаться появления заказа в «В работе».
- `get_total_orders` — общее количество заказов.
- `get_total_today` — количество заказов, выполненных сегодня.

### Тесты

#### Конструктор бургеров(test_counters)
- `test_drag_ingredient_increases_counter` — проверка увеличения счётчика ингредиента при перетаскивании.

#### Модальное окно ингредиента(test_modal_windows)
- `test_ingredient_modal_opens` — модалка открывается при клике на ингредиент.
- `test_ingredient_modal_closes` — модалка закрывается по крестику.

#### Навигация(test_navigation)
- `test_click_constructor` — переход по клику на «Конструктор».
- `test_click_feed` — переход по клику на «Лента заказов».

#### Лента заказов(test_order_feed)
- `test_total_orders_counter_increases` — создание заказа увеличивает счётчик «Выполнено за всё время».
- `test_today_orders_counter_increases` — создание заказа увеличивает счётчик «Выполнено за сегодня».
- `test_order_appears_in_progress` — номер заказа появляется в разделе «В работе».

## Фикстуры
- `driver` — инициализация браузеров Chrome и Firefox с максимизацией окна.
- `BasePage`, `MainPage`, `FeedPage` — страницы с методами взаимодействия и проверок.

## Локаторы

- `main_locators` — Содержит локаторы проекта