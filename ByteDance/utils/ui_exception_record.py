import time
import allure

def ui_exception_record(func):
    def inner(*args, **kwargs):
        # 获取被装饰函数/方法的 self，也即是实例对象
        # 通过 self 就可以拿到声明的实例变量
        # 前提条件：被装饰的方法是一个实例方法
        # 实例需要有实例变量 self.driver
        # 问题：被装饰还没有执行，还没有self.driver
        # 解决方案1：获取driver放在函数执行之后
        # 解决方案2：保证使用装饰器的时候，driver 已经声明
        driver = args[0].driver
        try:
            # 当被装饰函数/方法发生异常，就捕获并做数据记录
            return func(*args, **kwargs)
        except Exception as e:
            # 方案2
            # driver = args[0].driver
            # 出现异常的超级
            print(f"出现异常：{e}")
            # 截图操作
            timestamp = int(time.time())
            # 提前创建好 datas 路径
            image_path = f"./images/image_{timestamp}.PNG"
            page_source_path = f"./page_source/page_source_{timestamp}.html"
            # 截图
            driver.save_screenshot(image_path)
            # 将截图放入报告的数据中
            allure.attach.file(image_path, name='picture', attachment_type=allure.attachment_type.PNG)
            # 记录 page_source
            with open(page_source_path, "w", encoding='utf-8') as file:
                file.write(driver.page_source)
            # 将截图数据放入报告的数据中
            # llure.attachment_type.HTML  展示页面
            # llure.attachment_type.TEXT 展示页面源码
            allure.attach.file(page_source_path, name='pagesource', attachment_type=allure.attachment_type.HTML)
            raise e

    return inner
