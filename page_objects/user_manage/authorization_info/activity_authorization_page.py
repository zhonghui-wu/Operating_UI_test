# 用户管理 ==> 授权信息 ==> 活动授权页
from Operating_UI_test.common.base_page import BasePage


class OperatingActivityAuthorizationPage(BasePage):

    def is_have_msg(self):
        """
        判断是否有数据
        :return:
        """
        return self.isexist_element(self.page_first_msg)