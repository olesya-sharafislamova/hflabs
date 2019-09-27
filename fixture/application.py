
from selenium import webdriver
from fixture.appeal import AppealHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.appeal = AppealHelper(self)

    def open_appeal_page(self):
        wd = self.wd
        wd.get("http://hflabs.github.io/suggestions-demo/")

    def destroy(self):
        self.wd.quit()

