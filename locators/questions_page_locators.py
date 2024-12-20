from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    QUESTIONS_ABOUT_IMPORTANT = (By.XPATH, ".//div[text()='Вопросы о важном']")
    ANSWER_PRICE = (By.XPATH, ".//p[starts-with(text(), 'Сутки — 400 рублей']")
    # ANSWER_PRICE = (By.XPATH, ".//div[contains(@aria-disabled, 'true')]")
    ANSWER_FEW_SCOOTERS = (By.XPATH, ".//p[starts-with(text(), 'Пока что у нас так']")
    ANSWER_RENTAL_TIME = (By.XPATH, ".//p[starts-with(text(), 'Допустим, вы оформляете заказ']")
    ANSWER_RENTAL_TODAY = (By.XPATH, ".//p[starts-with(text(), 'Только начиная с завтрашнего дня']")
    ANSWER_EXTEND_ORDER = (By.XPATH, ".//p[starts-with(text(), 'Пока что нет!']")
    ANSWER_CHARGER = (By.XPATH, ".//p[contains(text(), 'с полной зарядкой']")
    ANSWER_CANCEL_ORDER = (By.XPATH, ".//p[contains(text(), 'пока самокат не привезли']")
    ANSWER_MKAD = (By.XPATH, ".//p[contains(text(), 'Всем самокатов']")

    @staticmethod
    def arrow_number(number):
        return By.XPATH, f'//div[@id="accordion__heading-{number}"]'

    @staticmethod
    def answer_number(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]'
