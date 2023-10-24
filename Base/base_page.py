import datetime

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from uitls.log_uitls import logger


class Basepage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)     # 隐式等待
        self.wait = WebDriverWait(self.driver, 10)  # 显示等待
        self.actions = ActionChains(self.driver)    # 鼠标动作链初始化

    def find_element(self, loc, condition='visibility',retry=1):
        """

        :param loc:定位内容
        :param condition: 默认visibility
        :param retry:重试次数，我写的1
        :return:
        """
        for time in range(retry+1):
            try:
                logger.info(f"当前定位：{loc}")
                if condition == 'visibility':
                    node = self.wait.until(EC.visibility_of_element_located(loc))
                else:
                    node = self.wait.until(EC.presence_of_element_located(loc))
                return node
            except Exception as e:
                errno_info = f"{loc}定位失败，错误信息{e}"
                logger.error(errno_info)
                if time < retry:
                    logger.info(f"正在重新定位，当前重试次数：{time+1}")
                else:
                    raise Exception(errno_info)

    def send_keys(self, loc, value, enter=False):
        """
        输入操作封装
        :param loc:元素定位
        :param value:输入项
        :return:
        """
        node = self.find_element(loc)
        node.clear()
        node.send_keys(value)
        logger.info(f"输入的内容为：{value}")
        if enter:
            node.send_keys(Keys.ENTER)
            logger.info(f"输入回车键")

    def click_buton(self, loc):
        """
        封装点击
        :param loc:
        :return:
        """
        node = self.find_element(loc)
        node.click()
        logger.info(f"点击按钮")

    def get_url(self, url=''):
        """
        请求网站
        :param url:
        :return:
        """
        self.driver.get(url)
        logger.info(f"打开网址：{url}")

    def close_driver(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.close()
        logger.info(f"关闭浏览器")

    def quit_driver(self):
        """
        退出浏览器
        :return:
        """
        self.driver.quit()
        logger.info(f"退出浏览器")

    def refesh(self):
        """
        刷新浏览器
        :return:
        """
        self.driver.refesh()
        logger.info(f"刷新浏览器")

    def switch_to_window(self, to_parent_window=False):
        """
        切换窗口
        :param to_parent_window:是否回到主窗口Ture为切换到主，False为切换其他窗口
        :return:
        """
        total = self.driver.window_handles
        if to_parent_window:
            self.driver.switch_to_window(total[0])
        else:
            current_window = self.driver.current_window_handles
            for window in total:
                if window != current_window:
                    self.driver.switch_to.window(window)

    def get_title(self):
        """
        获取网页title
        :return:
        """
        return self.driver.title

    def get_current_url(self):
        """
        获取当前url
        :return:
        """
        return self.driver.current_url

    def get_page_source(self):
        """
        获取网页源码
        :return:
        """
        return self.driver.page_source

    def get_text(self,loc):
        """
        获取元素文本
        :param loc:
        :return:
        """
        ele = self.find_element(loc)
        text = ele.text
        if text == "":
            text = ele.accessible_name
        logger.info(f"元素是{loc}的文本为{text}")
        return text

    def move_to_element(self, loc):
        """
        移动鼠标
        :param loc:
        :return:
        """
        ele = self.driver.move_to_element(loc)
        self.actions.move_to_element(ele).perform()
        logger.info(f"鼠标移动到{loc}位置")

    def drag_and_drop(self,loc_start, loc_end):
        """
        鼠标拖动
        :param loc_start:
        :param loc_end:
        :return:
        """
        start = self.find_element(loc_start)
        end = self.find_element(loc_end)
        self.actions.drag_and_drop(start, end).perform()
        logger.info(f"鼠标从{loc_start}拖动{loc_end}")

    def drag_and_drop_by_offset(self,loc, x, y):
        """

        :param loc:
        :param x:
        :param y:
        :return:
        """
        ele = self.find_element(loc)
        self.actions.drag_and_drop_by_offset(ele, x, y)
        logger.info(f"鼠标拖动")

    def select_by_index(self, loc, index):
        """
        根据下标获取select
        :param loc:
        :param index: 下标从0开始
        :return:
        """
        ele = self.find_element(loc)
        select = Select(ele)
        select.select_by_index(index)
        logger.info(f"根据下标{index}获取的select")

    def select_by_value(self, loc, value):
        """
        根据value值获取select
        :param loc:
        :param value:
        :return:
        """
        ele = self.find_element(loc)
        select = Select(ele)
        select.select_by_value(value)
        logger.info(f"根据下标{value}获取的select")

    def select_by_visiable_text(self, loc, visiable_text):
        """
        根据visiable_text值值获取select
        :param loc:
        :param visiable_text:visiable_text值
        :return:
        """
        ele = self.find_element(loc)
        select = Select(ele)
        select.select_by_visible_text(visiable_text)
        logger.info(f"根据下标{visiable_text}获取的select")

    def wait_ele_presence(self, loc, center=True):
        """

        :param loc:
        :param center:
        :return:
        """
        try:
            start = datetime.datetime.now()
            ele = self.wait.until(EC.presence_of_element_located(loc))
            end = datetime.datetime.now()
            logger.info("元素{}已存在，等待{}秒".format(loc,(end-start).seconds))
            self.driver.execute_script("argument[0].scrollIntoViewIfNeeded(argument[1]);", ele, loc)
            return ele
        except Exception:
            logger.error("元素不存在-{}".format(loc))
            raise

    def switch_t0_frame(self, index=0, to_parent_frame=False, to_default_frame=False):
        """

        :param index:
        :param to_parent_frame:
        :param to_default_frame:
        :return:
        """
        if to_parent_frame:
            self.driver.switch_to.parent_frame()
        elif to_default_frame:
            self.driver.switch_to.default_content()
        else:
            self.driver.switch_to.default_frame(index)
        logger.info(f'切换框架，to{index}')

    def popup_windows_operation(self, action='yes', send_info='',get_window_info=''):
        """
        弹窗操作
        :param action: 要执行的动作 yes or no
        :param send_info: 输入弹窗信息
        :param get_window_info: 获取弹窗信息
        :return:
        """
        if send_info:
            logger.info(f"在弹窗上输入信息：{send_info}")
            self.driver.switch_to.alert.send_keys(send_info)

        if get_window_info:
            popup_info = self.driver.switch_to.alert.text
            logger.info(f"获取弹窗的文本信息：{popup_info}")

        if action == 'yes':
            logger.info('在弹窗上确认')
            self.driver.switch_to.alert.accept()
        else:
            logger.info('在弹窗上取消')
            self.driver.switch_to.alert.dismiss()

    def back(self):
        """

        :return:
        """
        self.driver.back()
        logger.debug('退后')

    def forward(self):
        """

        :return:
        """
        self.driver.forward()
        logger.debug('前进')
