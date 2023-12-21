from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestInitialization:
    def __init__(self, driver):
        if driver == None:
            # 初始化 driver
            server = Service(executable_path=ChromeDriverManager().install())\
            # 1. 初始化driver
            self.driver = webdriver.Chrome(service=server)

        else:
            self.driver = driver

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def teardown_class(self):
        self.driver.quit()
    def open_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
