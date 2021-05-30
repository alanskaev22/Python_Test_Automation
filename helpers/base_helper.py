from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from helpers import constants


class BaseHelper:
    ValidationErrors = []

    @classmethod
    def init_driver(cls):
        driver = webdriver.Chrome(executable_path=r"C:\Users\Alan\Desktop\chromedriver_win32\chromedriver.exe");
        driver.get(constants.APP_URL)
        return driver

    @staticmethod
    def assertEqual(expected, actual, validationMessage, stopTestRun: bool = False):
        try:
            assert expected == actual, f'\n{validationMessage} \nActual: {expected} \nExpected: {actual}'
        except AssertionError as msg:
            BaseHelper.ValidationErrors.append(msg)

            if stopTestRun:
                raise msg

    @staticmethod
    def teardownTest(driver: WebDriver):
        driver.close()
        printErrors(BaseHelper.ValidationErrors)
        # assert BaseHelper.ValidationErrors == [], [printErrors(BaseHelper.ValidationErrors)]


def printErrors(err: BaseHelper.ValidationErrors):
    if len(err) > 0:
        print("\033[91m" + "\n\n============================= TEST FAILED. ERRORS: =============================")
        for error in err:
            print("\033[91m" + f"\nValidation Error {err.index(error) + 1}")
            print("\033[93m" + f"\n{str(error)}")
        print("\033[91m" + "\n\n============================= END OF ERRORS =============================")
        pytest.fail()
