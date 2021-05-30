from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    title = (By.ID, "welcome")
    introText = (By.CLASS_NAME, "introText")

    def get_title(self):
        return self.driver.find_element(*HomePage.title).text
