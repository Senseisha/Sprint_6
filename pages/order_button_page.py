import allure
from pages.base_page import BasePage
from locators.order_button_locators import ButtonLocators
from helper import generate_registration
from data import Credentials


class ButtonPage(BasePage):
    @allure.step("Проскроллить до кнопки Заказать")
    def scroll_to_bottom_button(self):
        self.scroll_to_element(ButtonLocators.BOTTOM_BUTTON)

    @allure.step("Кликнуть на нижнюю кнопку Заказать")
    def click_on_bottom_button(self):
        self.click_on_element(ButtonLocators.BOTTOM_BUTTON)

    @allure.step("Кликнуть на верхнюю кнопку Заказать")
    def click_on_top_button(self):
        self.click_on_element(ButtonLocators.TOP_BUTTON)

    @allure.step("Подождать загрузки страницы с формой заказа")
    def wait_to_order_page(self):
        self.wait_new_page(ButtonLocators.ORDER_PAGE)

    @allure.step("Заполнить поля формы Для кого самокат")
    def send_keys_to_input_field_scooter(self):
        name, last_name, address, phone_number = generate_registration()
        self.driver.find_element(*ButtonLocators.NAME).send_keys(name)
        self.driver.find_element(ButtonLocators.LAST_NAME[0], ButtonLocators.LAST_NAME[1]).send_keys(last_name)
        self.driver.find_element(ButtonLocators.ADDRESS[0], ButtonLocators.ADDRESS[1]).send_keys(address)
        self.click_on_element(ButtonLocators.STATION)
        self.driver.find_element(ButtonLocators.SELECTED_STATION[0], ButtonLocators.SELECTED_STATION[1]).click()
        self.driver.find_element(ButtonLocators.NUMBER[0], ButtonLocators.NUMBER[1]).send_keys(phone_number)

    @allure.step("Кликнуть на кнопку Далее")
    def click_on_button_next(self):
        self.click_on_element(ButtonLocators.BUTTON_NEXT)

    @allure.step("Подождать загрузки страницы Про аренду")
    def wait_to_order_page_about_rent(self):
        self.wait_new_page(ButtonLocators.RENT_PAGE)

    @allure.step("Заполнить поля формы Про аренду")
    def send_keys_to_input_field_rent(self):
        self.click_on_element(ButtonLocators.DATEPICKER)
        self.driver.find_element(*ButtonLocators.DATE).click()

        self.click_on_element(ButtonLocators.RENTAL_PERIOD)
        self.driver.find_element(*ButtonLocators.DROPDOWN_MENU).click()

    @allure.step("Заполнить поле Цвет самоката-черный жемчуг")
    def send_keys_to_input_black(self):
        self.driver.find_element(*ButtonLocators.BLACK).click()

    @allure.step("Заполнить поле Цвет самоката-серая безысходность")
    def send_keys_to_input_grey(self):
        self.driver.find_element(*ButtonLocators.GRAY).click()

    @allure.step("Заполнить поле Комментарий")
    def send_keys_to_input_comment(self):
        self.driver.find_element(*ButtonLocators.COMMENT).send_keys("Добавьте, пожалуйста, розовый цвет для самокатов")

    @allure.step("Кликнуть на кнопку Заказать")
    def click_on_order_button(self):
        self.click_on_element(ButtonLocators.ORDER_BUTTON)

    @allure.step("Подождать загрузки окна с подтверждением")
    def wait_to_verification(self):
        self.wait_new_page(ButtonLocators.VERIFICATION)

    @allure.step("Нажать на кнопку Да")
    def click_on_button_yes(self):
        self.click_on_element(ButtonLocators.BUTTON_YES)

    @allure.step("Проверить, что виден элемент всплывающего окна")
    def wait_to_popup_element(self):
        self.wait_for_element(ButtonLocators.ORDER_PLACED)

    @allure.step("Получить текст элемента")
    def get_popup_text(self):
        return self.driver.find_element(*ButtonLocators.ORDER_PLACED_TEXT).text

    @allure.step("Нажать на кнопку Статус заказа")
    def click_on_button_status(self):
        self.click_on_element(ButtonLocators.STATUS_BUTTON)

    @allure.step("Ввести номер заказа")
    def send_keys_to_input_number(self):
        self.driver.find_element(*ButtonLocators.ORDER_NUMBER).send_keys(Credentials.number)

    @allure.step("Нажать на кнопку Go")
    def click_on_button_go(self):
        self.click_on_element(ButtonLocators.BUTTON_GO)

    @allure.step("Подождать загрузки страницы с заказом")
    def wait_to_go_to_page_with_order(self):
        self.wait_new_page(ButtonLocators.PAGE_WITH_ORDER)

    @allure.step("Кликнуть на логотип Самоката")
    def click_on_button_logo_scooter(self):
        self.click_on_element(ButtonLocators.SCOOTER)

    @allure.step("Подождать загрузки главную страницу")
    def wait_to_go_to_main_page(self):
        self.wait_new_page(ButtonLocators.MAIN_PAGE)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_on_button_logo_yandex(self):
        self.click_on_element(ButtonLocators.YANDEX)

    @allure.step("Подождать загрузки главной страницы Дзена")
    def wait_to_go_to_page_dzen(self):
        href = self.driver.find_element(*ButtonLocators.YANDEX).get_attribute('href')
        self.driver.get(href)
        self.wait_new_page(ButtonLocators.DZEN)
