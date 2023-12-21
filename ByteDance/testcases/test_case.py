import allure
import pytest

from test_user.ByteDance.page.main_page import MainPage
from test_user.ByteDance.page.message_list_page import MessageList

datas=[[17722844353,'a1234567a','一','tester1'],[13396541594, 'a1234567a','1234567890','tester2']]
@allure.feature('飞书 web 端发送消息')
class TestCase:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.close_browser()

    @allure.story('联系人发送消息')
    @allure.step('发送消息成功')
    @pytest.mark.parametrize('user',datas)
    def test_send_message(self,user):
        message = self.main.goto_login().login(user[0],user[1]).go_to_message().message_menu().user_info().send_message(user[2]).message_info()
        assert user[2] in message
        name = MessageList().message_user()
        assert user[3] in name
        MessageList().over_message()
        MessageList().login_out()
