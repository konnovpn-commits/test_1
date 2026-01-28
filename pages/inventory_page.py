from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    # Локаторы
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_title(self):
        """Получить заголовок страницы"""
        return self.find_element(self.PRODUCTS_TITLE).text
    
    def is_cart_visible(self):
        """Проверить видимость корзины"""
        return self.is_element_visible(self.SHOPPING_CART)
    
    def logout(self):
        """Выйти из системы"""
        self.click(self.MENU_BUTTON)
        self.wait.until(
            lambda d: self.is_element_visible(self.LOGOUT_LINK)
        )
        self.click(self.LOGOUT_LINK)
    
    def get_url(self):
        """Получить URL страницы"""
        return self.get_current_url()
           
    def is_page_loaded(self):
        """Проверить, что страница загрузилась"""
        try:
            return self.is_element_visible(self.PRODUCTS_TITLE) and \
                   self.is_element_visible(self.SHOPPING_CART)
        except:
            return False