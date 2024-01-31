# 产品管理 ==> 产品商城 ==> 直充权益产品
from Operating_UI_test.common.base_page import BasePage


class OperatingUserFillContinuouslyProductPage(BasePage):

    def is_have_msg(self):
        """
        判断是否有数据
        :return:
        """
        return self.isexist_element(self.page_first_msg)