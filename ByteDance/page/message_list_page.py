import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from test_user.ByteDance.base.base_page import BasePage


class MessageList(BasePage):
    __MESSAGE_BUTTON = (By.CSS_SELECTOR, 'section>section:nth-child(5)>div>svg')
    __USER_FRIEND = (By.CSS_SELECTOR, '.contactPageNav_item.EXTERNAL_CONTACT  .larkc-sidebar-card-name')
    __FRIEND_USER = (By.CSS_SELECTOR, '.contactCard')
    __USER_INFO = (By.CSS_SELECTOR, '.larkc-usercard__ctas>button:nth-child(1)>svg>path')
    __USER = (By.CSS_SELECTOR, '.feed-slider>div:nth-child(1) .list_items>div:nth-child(2)')
    __USER_TEST = (By.CSS_SELECTOR, '.feedCard.feedCard_active')
    __MESSAGE_LIST = (By.CSS_SELECTOR, '.text-only')
    __MESSAGE_INPUT = (By.CSS_SELECTOR, '.lark-editor.lark-empty')
    __MESSAGE_USER = (By.CSS_SELECTOR, '.chatWindow_groupName.lark-drag-disable')
    __OVER_MESSAGE = (By.CSS_SELECTOR, '.feed-slider>div:nth-child(1) .list_items>div:nth-child(2)>div>div>div>div:nth-child(3)>.larkc-svg-icon')
    __UN_LOGIN = (By.CSS_SELECTOR, '.appNavbar .larkc-avatar-img')
    __LOGINOUT = (By.CSS_SELECTOR, '.tenantUserCard_links>div:nth-child(6)')
    __LOGINOUT_OK = (By.CSS_SELECTOR, '.larkc-btn.larkc-btn-normal.larkc-btn-error.larkc-btn-large')
    @allure.step('进入消息列表并点击通讯录')
    def message_menu(self):
        self.windows_page()
        # 检测 通讯录菜单并进入
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__MESSAGE_BUTTON))
        self.find_ele(self.__MESSAGE_BUTTON).click()
        return self

    @allure.step('查找联系人并进入聊天界面')
    def user_info(self):
        self.windows_page()
        # 检测 外部联系人并选择联系人
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__USER_FRIEND))
        self.find_ele(self.__USER_FRIEND).click()
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__FRIEND_USER))
        self.find_ele(self.__FRIEND_USER).click()
        # 检测 联系人信息卡片
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__USER_INFO))
        self.find_ele(self.__USER_INFO).click()
        return self


    @allure.step('发送消息')
    def send_message(self,message):
        self.windows_page()
        # 检测 消息列表中此用户已显示，选择并打开聊天框
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__USER))
        self.find_ele(self.__USER).click()
        # 检测聊天框已打开并发送消息
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__MESSAGE_INPUT))
        self.find_ele(self.__MESSAGE_INPUT).send_keys(message)
        self.find_ele(self.__MESSAGE_INPUT).send_keys(Keys.ENTER)
        return self

    @allure.step('勾选结束对话')
    def over_message(self):
        self.windows_page()
        user = self.find_ele(self.__USER)
        self.move_goto(user)
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__OVER_MESSAGE))
        self.find_ele(self.__OVER_MESSAGE).click()

    @allure.step('获取已发送的消息记录')
    def message_info(self):
        self.windows_page()
        ele = []
        eles = self.find_eles(self.__MESSAGE_LIST)
        for item in eles:
            ele.append(item.text)
        return ele

    @allure.step('获取当前通信人员信息')
    def message_user(self):
        self.windows_page()
        name = self.find_ele(self.__MESSAGE_USER)
        return name.text


    @allure.step('退出登录')
    def login_out(self):
        self.find_ele(self.__UN_LOGIN).click()
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__LOGINOUT))
        self.find_ele(self.__LOGINOUT).click()
        self.wait_ele(expected_conditions.element_to_be_clickable(self.__LOGINOUT_OK))
        self.find_ele(self.__LOGINOUT_OK).click()


