from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Найти элемент с явным ожиданием"""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )
    
    def find_elements(self, locator):
        """Найти несколько элементов"""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f"Элементы {locator} не найдены"
        )
    
    def click(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        element.click()
    
    def send_keys(self, locator, text):
        """Ввести текст"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
    
    def is_element_visible(self, locator):
        """Проверить видимость элемента"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False