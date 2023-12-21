import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from test_user.ByteDance.base.base_page import BasePage
from test_user.ByteDance.page.message_list_page import MessageList


class MainPage(BasePage):
    Index_URL = "https://www.feishu.cn/"
    __DEMO = (By.CSS_SELECTOR, 'body .hc_Popup')
    __DEMO_CLOSE = (By.CSS_SELECTOR, '.hc_Popup-content path')
    __LOGIN_TEXT = (By.CSS_SELECTOR, '#app   a:nth-child(9)')
    __LOGIN_WAYS = (By.CSS_SELECTOR, '.switch-login-mode-box')
    __LOGIN_WAY = (By.CSS_SELECTOR, '.tooltip-content')

    __PHONE_INPUT = (By.CSS_SELECTOR, '.mobile-input-phone')
    __INPUT_CHECKBOX = (By.CSS_SELECTOR, '.ud__checkbox__input')
    __NEXT_BUTTON = (By.CSS_SELECTOR,
                     '.ud__button.ud__button--filled.ud__button--filled-default.ud__button--size-lg.ud__button--block._pp-ud-btn-block')
    __PWD_INPUT = (By.CSS_SELECTOR, '.ud__input-password-input-wrap>.ud__native-input')
    __NEXT_LOGIN = (By.CSS_SELECTOR,
                    '.step-box__footer>.ud__button.ud__button--filled.ud__button--filled-default.ud__button--size-lg.ud__button--block._pp-ud-btn-block')
    __MESSAGE_BUTTON = (By.CSS_SELECTOR, '.universe-icon._pp-product-icon>svg>path')
    __MESSAGE = (By.XPATH, '/html/body/div[3]/div/div/div/div/div[1]/ul/li[1]')

    @allure.step("打开飞书官网并跳转登录页面")
    def goto_login(self):
        # 进入首页
        self.open_url(self.Index_URL)
        while True:
            # 检查 首次打开时出现的弹窗属性
            self.wait_ele(expected_conditions.element_to_be_clickable(self.__DEMO))
            demo = self.find_ele(self.__DEMO)
            # 获取指定窗口的style属性值
            style = demo.get_attribute('style')
            list = style.split(':')
            # 根据display属性值判断是都需要点击关闭按钮
            if list[1] == ' flex;':
                self.find_ele(self.__DEMO_CLOSE).click()
            else:
                break
        # 跳转登录
        self.find_ele(self.__LOGIN_TEXT).click()
        # 检测登录方式元素已存在
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__LOGIN_WAYS))
        # 鼠标悬停 获取 当前登录方式
        tests = self.find_ele(self.__LOGIN_WAYS)
        self.move_goto(tests)
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__LOGIN_WAY))
        text = self.find_ele(self.__LOGIN_WAY)
        txt = text.text
        if txt == '账号登录':
            # 判断为当前方式是 扫码登录模式，切换为账号登录模块
            self.find_ele(self.__LOGIN_WAYS).click()
        return self

    @allure.step('账号登录')
    def login(self, phone, password):
        # 手机号输入账号并勾选协议
        self.find_ele(self.__PHONE_INPUT).send_keys(phone)
        self.find_ele(self.__INPUT_CHECKBOX).click()
        # 点击下一步
        self.find_ele(self.__NEXT_BUTTON).click()
        # 检测 密码输入框元素并输入密码
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__PWD_INPUT))
        self.find_ele(self.__PWD_INPUT).send_keys(password)
        # 点击下一步登录
        self.find_ele(self.__NEXT_LOGIN).click()
        return self

    @allure.step('跳转消息页面')
    def go_to_message(self):
        # 检测 九宫格按钮并点击
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__MESSAGE_BUTTON))
        self.find_ele(self.__MESSAGE_BUTTON).click()
        # 检测 消息按钮并点击
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__MESSAGE))
        self.find_ele(self.__MESSAGE).click()
        return MessageList(self.driver)