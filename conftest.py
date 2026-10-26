import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем опцию для выбора языка, по умолчанию английский ('en')
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, ru, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")
    print(f"\nstart chrome browser for test with language {user_language}..")
    
    # Настраиваем Options для Chrome, чтобы передать язык
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    # Инициализируем браузер с настройками
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()
