# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 15:52
# @Author  : Cr
# @File    : editUser.py
import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from businessView.loginView import LoginView


class EditUser(Common):
    userIcon = (By.ID,'com.fangmi.weilan:id/user_icon')
    userimage = (By.ID,'com.fangmi.weilan:id/userImageLayout')
    nickname = (By.ID,'com.fangmi.weilan:id/nickNameLayout')
    sex = (By.ID,'com.fangmi.weilan:id/sexLayout')
    select_sex = (By.ID,'com.fangmi.weilan:id/select_dialog_listview')




    def editUser(self):
        logging.info('开始测试')
        self.driver.find_element(*self.userIcon).click()
        self.driver.find_element(*self.userimage).click()

if __name__ == '__main__':
    driver=appium_desired()
    l = LoginView(driver)
    l.login_action('18380477273','111111')
    e = EditUser(driver)
    e.editUser()