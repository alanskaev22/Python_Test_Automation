from helpers.home_helper import HomeHelper
from helpers.base_helper import BaseHelper


class TestSuccess(BaseHelper):
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = cls.init_driver()
        cls._helper = HomeHelper(cls.driver)

    @classmethod
    def teardown_class(cls):
        BaseHelper.teardownTest(cls.driver)

    def test_one(self):
        self._helper.validatePageTitle("Welcome to Allamuchy Auto Partss")
        self._helper.validatePageTitle("Welcome to Allamuchy Auto Paaas")
