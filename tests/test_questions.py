import allure
import pytest
from pages.questions_page import QuestionsPage
from data import Data


class TestPageQuestionsAboutImportant:
    @allure.title("Тест на соответствие текста к вопросам")
    @pytest.mark.parametrize('arrow_number, expected_text', Data.arrow_names)
    def test_questions_price(self, driver, arrow_number, expected_text):
        questions_page = QuestionsPage(driver)

        questions_page.scroll_to_questions()
        questions_page.load_main_page()
        questions_page.click_on_arrow(arrow_number)

        assert questions_page.check_correct_text(arrow_number, expected_text)


