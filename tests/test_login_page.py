# tests/test_login_page.py
import pytest
import allure
import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import Config

@allure.epic("Авторизация")
@allure.feature("Логин")
class TestLogin:
    
    @allure.title("Успешный логин стандартным пользователем")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke  # Добавить маркер
    def test_successful_login(self, login_page):
        """Тест успешной авторизации"""
        with allure.step("Ввести валидные учетные данные"):
            login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        
        with allure.step("Проверить переход на страницу инвентаря"):
            inventory_page = InventoryPage(login_page.driver)
            assert inventory_page.is_page_loaded()
            assert "inventory.html" in inventory_page.get_current_url()
        
        with allure.step("Проверить отображение элементов на странице"):
            assert inventory_page.get_title() == "Products"
            assert inventory_page.is_cart_visible()
    
    @allure.title("Логин с неверным паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression  # Добавить маркер
    def test_wrong_password(self, login_page):
        """Тест авторизации с неверным паролем"""
        with allure.step("Ввести неверный пароль"):
            login_page.login(Config.STANDARD_USER, Config.INVALID_PASSWORD)
        
        with allure.step("Проверить сообщение об ошибке"):
            error_text = login_page.get_error_message()
            assert "Username and password do not match" in error_text
    
    @allure.title("Логин заблокированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_locked_user(self, login_page):
        """Тест авторизации заблокированным пользователем"""
        with allure.step("Ввести данные заблокированного пользователя"):
            login_page.login(Config.LOCKED_USER, Config.PASSWORD)
        
        with allure.step("Проверить сообщение об ошибке"):
            error_text = login_page.get_error_message().lower()
            assert "locked out" in error_text
    
    @allure.title("Логин с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_empty_fields(self, login_page):
        """Тест авторизации с пустыми полями"""
        with allure.step("Нажать кнопку логина без ввода данных"):
            login_page.login(Config.EMPTY, Config.EMPTY)  # Использовать константу
        
        with allure.step("Проверить сообщение об ошибке"):
            error_text = login_page.get_error_message()
            assert "Username is required" in error_text
    
    @allure.title("Логин пользователем с проблемами производительности")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.slow
    @pytest.mark.performance  # Добавить маркер
    def test_performance_user(self, login_page):
        """Тест авторизации пользователем с проблемами производительности"""
        with allure.step("Ввести данные пользователя с проблемами производительности"):
            start_time = time.time()  # Измерить время
            login_page.login(Config.PERFORMANCE_USER, Config.PASSWORD)
        
        with allure.step("Проверить успешный вход (с увеличенным таймаутом)"):
            # Увеличиваем таймаут для медленного пользователя
            inventory_page = InventoryPage(login_page.driver)
            
            # Явное ожидание загрузки
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            
            wait = login_page.wait
            wait.until(
                EC.url_contains("inventory.html"),
                message="Не удалось перейти на inventory страницу"
            )
            
            # Проверяем загрузку
            assert inventory_page.is_page_loaded()
            
            # Логируем время выполнения
            load_time = time.time() - start_time
            allure.attach(
                f"Время загрузки для performance_glitch_user: {load_time:.2f} секунд",
                name="Время выполнения",
                attachment_type=allure.attachment_type.TEXT
            )
            
            print(f"Performance test completed in {load_time:.2f} seconds")