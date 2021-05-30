from models.home_page import HomePage
from helpers.base_helper import *


class HomeHelper:
    def __init__(self, driver):
        self.driver = driver
        self.homePage = HomePage(driver)

    def validatePageTitle(self, title):
        actualTitle = self.homePage.get_title()
        BaseHelper.assertEqual(title, actualTitle, "Home page title is not valid.", True)
        return self
