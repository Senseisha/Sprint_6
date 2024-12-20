import allure
from pages.base_page import BasePage
from locators.questions_page_locators import QuestionsPageLocators


class QuestionsPage(BasePage):
    @allure.step("Подождать видимость элемента Вопросы о важном")
    def load_main_page(self):
        self.wait_for_element(QuestionsPageLocators.QUESTIONS_ABOUT_IMPORTANT)

    @allure.step("Проскроллить до раздела с вопросами")
    def scroll_to_questions(self):
        self.scroll_to_element(QuestionsPageLocators.QUESTIONS_ABOUT_IMPORTANT)

    @allure.step("Кликнуть на стрелочку с вопросом")
    def click_on_arrow(self, arrow_number):
        self.click_on_element(QuestionsPageLocators.arrow_number(arrow_number))

    @allure.step("Проверить соответствие текста для вопроса")
    def check_correct_text(self, arrow_number, expected_text, timeout=10):
        actually_text = self.wait_for_element(QuestionsPageLocators.answer_number(arrow_number), timeout).text
        return actually_text == expected_text
