from selenium.webdriver.common.by import By


class ButtonLocators:
    MAIN_PAGE = (By.XPATH, ".//div[text()='Привезём его прямо к вашей двери,']")
    TOP_BUTTON = (By.XPATH, ".//button[text()='Заказать']")
    BOTTOM_BUTTON = (By.XPATH, ".//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")

    # Для кого самокат
    ORDER_PAGE = (By.XPATH, ".//div[text()='Для кого самокат']")
    NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    LIST_STATION = (By.XPATH, ".//class='select-search__options'")
    SELECTED_STATION = (By.XPATH, "//li[@class='select-search__row']/button")
    NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")


    # Про аренду
    RENT_PAGE = (By.XPATH, ".//div[text()='Про аренду']")
    DATEPICKER = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    DATE = (By.XPATH, ".//div[contains(@class, 'react-datepicker__day--today')]")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-root")
    DROPDOWN_MENU = (By.XPATH, "//div[@class='Dropdown-option']")
    BLACK = (By.XPATH, "//label[@for='black']")
    GRAY = (By.XPATH, "//label[@for='grey']")
    COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class,'Order_Buttons')]/button[text()='Заказать']")

    # Всплывающее окно
    VERIFICATION = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_PLACED = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    ORDER_PLACED_TEXT = (By.XPATH, "//div[text()='Заказ оформлен']")


    # Ввод номера заказа
    STATUS_BUTTON = (By.XPATH, ".//button[text()='Статус заказа']")
    ORDER_NUMBER = (By.XPATH, ".//input[@placeholder='Введите номер заказа']")
    BUTTON_GO = (By.XPATH, ".//button[text()='Go!']")

    # Страница с заказом
    PAGE_WITH_ORDER = (By.XPATH, "//button[text()='Отменить заказ']")

    # Логотипы
    SCOOTER = (By.XPATH, "//a[@href='/']")
    YANDEX = (By.XPATH, "//a[@href='//yandex.ru']")
    DZEN = (By.XPATH, "//header[@id='dzen-header']")


