# 用户管理 ==> 收货地址页
from Operating_UI_test.common.base_page import BasePage
from time import sleep


class OperatingAddressPage(BasePage):

    def is_have_msg(self):
        """
        判断是否有数据
        :return:
        """
        return self.isexist_element(self.page_first_msg)
