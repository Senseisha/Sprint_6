import allure
from pages.order_button_page import ButtonPage
from curl import *


class TestTopButton:
    @allure.title("Тест успешного заказа через верхнюю кнопку с выбором черного цвета самоката")
    def test_successful_order_with_top_button_with_black_colour(self, driver):
        top_button_page = ButtonPage(driver)

        top_button_page.click_on_top_button()

        top_button_page.wait_to_order_page()
        top_button_page.send_keys_to_input_field_scooter()
        top_button_page.click_on_button_next()

        top_button_page.wait_to_order_page_about_rent()
        top_button_page.send_keys_to_input_field_rent()
        top_button_page.send_keys_to_input_black()
        top_button_page.click_on_order_button()

        top_button_page.wait_to_verification()
        top_button_page.click_on_button_yes()
        top_button_page.wait_to_popup_element()
        popup_text = top_button_page.get_popup_text()

        assert popup_text.startswith("Заказ оформлен")

    @allure.title("Тест успешного заказа через верхнюю кнопку без выбора цвета")
    def test_successful_order_with_top_button_without_colour(self, driver):
        top_button_order_page = ButtonPage(driver)

        top_button_order_page.click_on_top_button()
        top_button_order_page.wait_to_order_page()
        top_button_order_page.send_keys_to_input_field_scooter()
        top_button_order_page.click_on_button_next()

        top_button_order_page.wait_to_order_page_about_rent()
        top_button_order_page.send_keys_to_input_field_rent()
        top_button_order_page.click_on_order_button()

        top_button_order_page.wait_to_verification()
        top_button_order_page.click_on_button_yes()
        top_button_order_page.wait_to_popup_element()
        popup_text = top_button_order_page.get_popup_text()

        assert popup_text.startswith("Заказ оформлен")


class TestBottomButton:
    @allure.title(
        "Тест успешного заказа через нижнюю кнопку с выбором черного цвета самоката и с добавлением комментария")
    def test_successful_order_with_bottom_button(self, driver):
        bottom_button_page = ButtonPage(driver)

        bottom_button_page.scroll_to_bottom_button()
        bottom_button_page.click_on_bottom_button()

        bottom_button_page.wait_to_order_page()
        bottom_button_page.send_keys_to_input_field_scooter()
        bottom_button_page.click_on_button_next()

        bottom_button_page.wait_to_order_page_about_rent()
        bottom_button_page.send_keys_to_input_field_rent()
        bottom_button_page.send_keys_to_input_grey()
        bottom_button_page.send_keys_to_input_comment()
        bottom_button_page.click_on_order_button()

        bottom_button_page.wait_to_verification()
        bottom_button_page.click_on_button_yes()
        bottom_button_page.wait_to_popup_element()
        bottom_button_page.wait_to_popup_element()
        popup_text = bottom_button_page.get_popup_text()

        assert popup_text.startswith("Заказ оформлен")


class TestGoToLogo:
    @allure.title("Тест успешного перехода на главную страницу через логотип Самоката после оформления заказа")
    def test_successful_transition(self, driver):
        logo_button_scooter = ButtonPage(driver)

        logo_button_scooter.click_on_button_status()
        logo_button_scooter.send_keys_to_input_number()
        logo_button_scooter.click_on_button_go()
        logo_button_scooter.wait_to_go_to_page_with_order()
        logo_button_scooter.click_on_button_logo_scooter()
        logo_button_scooter.wait_to_go_to_main_page()

        assert driver.current_url == main_site + '/'

    @allure.title("Тест успешного перехода на главную страницу Дзена через логотип Яндекса после оформления заказа")
    def test_successful_transition(self, driver):
        logo_button = ButtonPage(driver)

        logo_button.click_on_button_status()
        logo_button.send_keys_to_input_number()
        logo_button.click_on_button_go()
        logo_button.wait_to_go_to_page_with_order()
        logo_button.click_on_button_logo_yandex()

        logo_button.wait_to_go_to_page_dzen()

        assert driver.current_url.startswith(dzen)
