import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====开始执行自动化测试====')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('====测试执行完成====')
        sleep(5)
        self.driver.close_app()