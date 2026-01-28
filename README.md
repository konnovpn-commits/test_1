# SauceDemo Automated Tests
Описание
Автоматизированные тесты авторизации для [SauceDemo](https://www.saucedemo.com/).

# Тестовые сценарии:
Успешный логин (standard_user)  
Логин с неверным паролем  
Логин заблокированного пользователя  (locked_out_user)  
Логин с пустыми полями  
Логин пользователем (performance_glitch_user)  

# Быстрый запуск:
bash
# Собрать и запустить тесты в Docker
docker build -t saucedemo-tests .  
docker run saucedemo-tests  
Результаты  
Все 5 тестов успешно проходят в Docker контейнере.  

# Технологии:
Python 3.10  
Selenium  
Page Object Pattern  
Pytest  
Allure отчеты  
Docker  

# Структура проекта:
text
tests/test_login_page.py    # Тесты  
pages/                      # Page Object  
utils/config.py             # Конфигурация  
conftest.py                 # Фикстуры  
requirements.txt            # Зависимости  
Dockerfile                  # Контейнеризация  
pytest.ini                  # Конфиг тестов  
Allure отчеты  
bash  

# Сгенерировать отчеты
docker run -v "%cd%"/allure-results:/app/allure-results saucedemo-tests pytest --alluredir=/app/allure-results

# Запуск с детальным выводом
docker run saucedemo-tests pytest -v

# Для удобства добавлен pytest.ini

