from common.myunit import StartEnd
from businessView.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):
    csv_file='../data/account.csv'

    #@unittest.skip('test_login_pass')
    def test_login_pass(self):
        logging.info('=====test_login_pass======')
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,1)

        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())


    #@unittest.skip('test_login_error')
    def test_login_error(self):
        logging.info('======test_login_error=====')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)

        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus(),msg='login fail!')

if __name__ == '__main__':
    unittest.main()