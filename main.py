from webbrowser import Chrome

from selene import browser, be, have, Config
from selene.support import by

browser.open('https://ya.ru')
if browser.element(by.text('Принять все')).matching(be.visible):
   browser.element(by.text('Принять все')).click()
browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search-result"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))