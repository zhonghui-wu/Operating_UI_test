# 用户管理 ==> 用户信息 ==> 农行用户页
from Operating_UI_test.common.base_page import BasePage
from time import sleep


class OperatingABCUserPage(BasePage):

    def is_have_msg(self):
        """
        判断是否有数据
        :return:
        """
        return self.isexist_element(self.page_first_msg)
