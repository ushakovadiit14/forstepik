import time
from selenium.webdriver.common.by import By

def test_guest_can_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза 30 секунд, чтобы рецензент мог визуально оценить перевод кнопки (например, на французском)
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину по ее уникальному CSS-классу
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка действительно отображается на странице
    assert button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена на странице"
