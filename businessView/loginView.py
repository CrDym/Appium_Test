import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):

    mineBtn = (By.ID,'com.fangmi.weilan:id/mine')
    user = (By.ID,'com.fangmi.weilan:id/user_name')
    loginPwd = (By.ID,'com.fangmi.weilan:id/login_pwd')

    username_type=(By.ID,'com.fangmi.weilan:id/et_user_name')
    password_type=(By.ID,'com.fangmi.weilan:id/et_possword')
    loginBtn=(By.ID,'com.fangmi.weilan:id/login')
    userb = (By.ID,'com.fangmi.weilan:id/user_b')
    username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    mymoreButton=(By.ID,'com.fangmi.weilan:id/myMore')
    logoutBtn=(By.ID,'com.fangmi.weilan:id/exit_btn')




    def login_action(self,username,password):
        logging.info('============滑动跳过引导页==============')
        for i in range(2):
            self.swipeLeft()
        self.check_openBtn()

        logging.info('============开始登录==============')

        logging.info('click mineBtn')
        self.driver.find_element(*self.mineBtn).click()

        logging.info('click userBtn')
        self.driver.find_element(*self.user).click()

        logging.info('click loginPwd')
        self.driver.find_element(*self.loginPwd).click()

        logging.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    def check_loginStatus(self):
        logging.info('====检查登录结果======')
        try:
            self.driver.find_element(*self.userb)
        except NoSuchElementException:
            logging.error('登录失败!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('登录成功!')
            self.getScreenShot('login success')
            self.logout_action()

            return True

    def logout_action(self):
        logging.info('=====退出登录======')
        self.driver.find_element(*self.mymoreButton).click()
        self.driver.find_element(*self.logoutBtn).click()




if __name__ == '__main__':
    driver=appium_desired()
    # l=LoginView(driver)
    # l.login_action('18380477273','111111')
    # l.check_loginStatus()