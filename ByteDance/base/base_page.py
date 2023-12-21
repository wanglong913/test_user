import os
import time

import allure
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from test_user.ByteDance.utils.log_utiles import logger


class BasePage:
    def __init__(self, base_driver:WebDriver=None):
        if base_driver == None:
            # 初始化 driver
            server = Service(executable_path=ChromeDriverManager().install())
            # 1.初始化driver
            self.driver = webdriver.Chrome(service=server)
            # 2. 添加隐式等待
            self.driver.implicitly_wait(5)
            # 3. 最大化窗口
            self.driver.maximize_window()
        else:
            self.driver = base_driver

    def open_url(self, url):
        # 打开测试目标页面
        with allure.step(f'打开url={url}'):
            logger.info(f'打开url={url}')
            self.driver.get(url)

    def close_browser(self):
        # 关闭网页与服务
        with allure.step('关闭浏览器'):
            logger.info('关闭浏览器')
            self.driver.quit()

    def windows_page(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])


    def wait_ele(self, method, timeout=10):
        # method 等待条件
        try:
            ele = WebDriverWait(self.driver, timeout).until(method)
        except Exception as e:
            ele =None
            # 截图
            self.screnn_image()
            # 保存页面
            self.save_page_source()
        return ele

    def find_ele(self,by,value=None):
        # 定位多个元素与
        try:
            if value == None:
                logger.info(f'定位单个元素，定位详情：{by}')
                ele = self.driver.find_element(*by)
            else:
                logger.info(f'定位单个元素，定位方式是{by}，定位表达式是{value}')
                ele = self.driver.find_element(by,value)
        except Exception as e:
            ele = None
            logger.info(f'单个元素没有找到，{e}')
            # 截图
            self.screnn_image()
            # 保存 page_source
            self.save_page_source()
        return ele

    def find_eles(self,by,value=None):
        # 定位多个元素
        if value == None:
            logger.info(f'定位多个元素，定位方式为{by}')
            ele = self.driver.find_elements(*by)
        else:
            logger.info(f'定位多个元素，定位方式为{by}，定位表达式为{value}')
            ele = self.driver.find_elements(by,value)
        return ele

    def move_goto(self,by):
        if by == None:
            logger.info(f'移动元素时没有找到元素。{by}')
        else:
            logger.info(f'移动的目标元素，定位方式为{by}')
            ActionChains(self.driver).move_to_element(by).perform()

    def screnn_image(self):
        # 截图并保存
        now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        image_name = f'{now_time}.png'
        # 拼接图片路径
        image_path = f'{self.get_path("images")}\\{image_name}'
        # 保存截图
        self.driver.save_screenshot(image_path)
        # 把截图加入报告中
        allure.attach.file(image_path, name='查找元素异常截图',attachment_type=allure.attachment_type.PNG)
        return image_path

    def save_page_source(self):
        # 页面源码
        now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
        page_source_name = f'{now_time}.html'
        # 拼接源代码路径
        page_source_path = f'{self.get_path("page_source")}\\{page_source_name}'
        # 保存源码
        with open(page_source_path, 'w', encoding='utf-8') as f:
            f.write(self.driver.page_source)
        # 添加源码到报告中
        allure.attach.file(page_source_path,name='查找异常页面源码',attachment_type=allure.attachment_type.TEXT)
        return page_source_path

    def get_path(self, path_name=None):
        '''获取绝对路径'''
        # 获取当前文件目录
        root_path = os.path.dirname(os.path.abspath(__file__))
        # 拼接当前要输出日志的路径
        log_path = os.sep.join([root_path,'..',path_name])
        return log_path






