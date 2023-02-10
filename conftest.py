import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(name='all_pets')
def open_all_pets():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.set_window_size(1920, 1080)
    """Переходим на страницу авторизации"""
    driver.get('http://petfriends.skillfactory.ru/login')
    """Вводим email"""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(
        'cubaka19m@mail.ru')
    """Вводим пароль"""
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "pass"))).send_keys("chubaka123")
    """Нажимаем на кнопку входа в аккаунт"""
    driver.find_element_by_css_selector('button[type="submit"]').click()

    return driver


@pytest.fixture(name='my_pets')
def open_my_pets(all_pets):
    all_pets.implicitly_wait(10)
    all_pets.get('https://petfriends.skillfactory.ru/my_pets')

    return all_pets