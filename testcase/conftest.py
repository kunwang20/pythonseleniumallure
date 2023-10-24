import allure
import pytest
from selenium import webdriver
from loc_page.login_page import LoginPage


@pytest.fixture(scope="session")
def driver_p():
    """
    conftest放置登录
    :return:
    """
    global driver_p
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.520dl.com/#/login')
    yield driver
    driver.close()

@pytest.fixture(scope="session")
def logged_driver(driver_p):
    """
    继承上面的登录页进行登录，除登录页用例外调用该conftest去进行前置
    :param driver_p:
    :return:
    """
    lp = LoginPage(driver_p)
    lp.send_keys(LoginPage.username, '')
    lp.send_keys(LoginPage.passwd, '')
    lp.click_buton(LoginPage.login_bt)
    yield driver_p
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    钩子函数用例失败截图
    :param item: 代表测试函数和方法，包含测试相关信息
    :param call: 包含测试函数执行的详细信息 结果，执行时间
    :return:
    """
    out = yield
    report = out.get_result()
    #print(f"测试报告：{report}")
    #print(f"步骤：{report.when}")
    #print(f"nodeid：{report.nodeid}")
    #print(f"运行结果：{report.outcome}")
    if report.when == 'call' and report.failed:
        allure.attach(driver_p.get_screent_shot_as_png(), "失败截图", attachment_type=allure.attachment_type.PNG)
