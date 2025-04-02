import pytest
from selenium import webdriver
from data.data import form_inputs

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(params = form_inputs)
def input_data(request):
    return request.param