import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import form_inputs

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    cookies = driver.find_element(By.ID, 'rcc-confirm-button')
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(cookies))
    cookies.click()
    yield driver
    driver.quit()

@pytest.fixture(params = form_inputs)
def input_data(request):
    return request.param