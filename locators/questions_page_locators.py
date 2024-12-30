from selenium.webdriver.common.by import By


class QuestionsPageLocators:
    QUESTIONS_ABOUT_IMPORTANT = (By.XPATH, ".//div[text()='Вопросы о важном']")

    @staticmethod
    def arrow_number(number):
        return By.XPATH, f'//div[@id="accordion__heading-{number}"]'

    @staticmethod
    def answer_number(number):
        return By.XPATH, f'//div[@id="accordion__panel-{number}"]'
