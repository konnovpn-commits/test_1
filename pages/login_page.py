from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")
    
    def login(self, username, password):
        """Выполнить вход"""
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Получить текст ошибки"""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.find_element(self.ERROR_MESSAGE).text
        return ""
    
    def clear_fields(self):
        """Очистить поля ввода"""
        self.find_element(self.USERNAME_INPUT).clear()
        self.find_element(self.PASSWORD_INPUT).clear()