# 安装文件
pip install DBUtils
pip install Jinja2
pip install allure-pytest
pip install selenium
pip install webdriver-manager
pip install appium-python-client


# 用例执行步骤：
1. 进入路径：test_user/ByteDance/testcases/test_case.py
2. 右键此文件，打开于 --> 终端
3. 终端执行命令：pytest ./test_case.py --alluredir=./result
4. 完成后查看测试报告，终端执行命令：allure serve ./result