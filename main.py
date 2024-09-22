from time import sleep

import pytest
from selene.api import *

@pytest.fixture
def size_browser():
   browser.driver().set_window_size(300, 400)
   yield
   browser.close()

@pytest.fixture
def open_browser():
   browser.open_url('https://google.com.ru')
   if browser.element(by.text('Принять все')).matching(be.visible):
      browser.element(by.text('Принять все')).click()

def test_needle_exist(open_browser,size_browser):
   browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
   browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_no_result(open_browser):
   browser.element('[name="q"]').should(be.blank).type('rsedgfhgjhkgfdgserwaasrdfhgjkgfddasfdgfhgjhkjgfdsafghjkg').press_enter()
   browser.element('[id="botstuff"]').should(have.text(' ничего не найдено. '))