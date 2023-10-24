from selenium.webdriver.common.by import By

from Base.base_page import Basepage
class LoginPage(Basepage):

    #   输入用户名
    username = (By.XPATH, '//*[@id="app"]/div[1]/form/div[1]/div/div[1]/input')
    #   输入密码
    passwd = (By.XPATH, '//*[@id="app"]/div[1]/form/div[2]/div/div[1]/input')
    #   点击登录
    login_bt = (By.XPATH, '//*[@id="app"]/div[1]/form/div[3]/div/button')
    #   错误断言：XX不存在
    err_username = (By.XPATH, '/html/body/div[2]/p')
    #   错误断言：用户名或密码错误
    err_passwd = (By.XPATH, "//p[contains(text(),'用户不存在/密码错误')]")
    #   断言没有输入用户名
    err_nousername = (By.XPATH, "//div[contains(text(),'请输入您的账号')]")
    #   断言没有输入密码
    err_nopasswd = (By.XPATH, "//div[contains(text(),'请输入您的密码')]")
