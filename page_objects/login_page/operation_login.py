# 运营端登录页
from Operating_UI_test.common.base_page import BasePage
from Operating_UI_test.config.config import operation_test_host, operation_test_username, tenant_code, operation_test_pwd
from Operating_UI_test.utils.all_path import img_code_path, operating_elements_yaml_path
from Operating_UI_test.utils.get_image_code import get_img_code
from Operating_UI_test.page_objects.home_page.operation_home_page import OperatingHomePage
from time import sleep


class OperatingLoginPage(BasePage):

    def open_login_page(self):
        self.open_url(operation_test_host)
        return self

    def login_sys(self):
        """
        执行登录操作
        :return: 首页
        """
        self.input_text(self.tenant_code, tenant_code)
        self.input_text(self.username, operation_test_username)
        self.input_text(self.pwd, operation_test_pwd)
        self.save_img(self.code_img)
        img_code = get_img_code(img_code_path)
        self.input_text(self.code, img_code)
        self.click_element(self.login_button)
        sleep(1)
        num = 0
        while True:
            try:
                login_button = self.get_element(self.login_button)
            except:
                break
            if login_button:
                self.click_element(self.code_img)
                self.save_img(self.code_img)
                img_code = get_img_code(img_code_path)
                self.input_text(self.code, img_code)
                self.click_element(self.login_button)
                sleep(2)
                if num == 30:
                    break
            else:
                break
        return OperatingHomePage(operating_elements_yaml_path)


if __name__ == '__main__':
    login = OperatingLoginPage(operating_elements_yaml_path)
    login.open_login_page().login_sys().logout()
    # sleep(1)
    # login.driver.quit()
