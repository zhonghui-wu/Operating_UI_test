from Operating_UI_test.common.base_page import BasePage
from Operating_UI_test.utils.all_path import operating_elements_yaml_path


class OperatingUserInfoEle(BasePage):
    """
    运营端首页右侧的用户信息页，获取信息用来校验修改信息是否正确
    """
    def get_username(self):
        """
        获取用户名称
        :return: 用户名称
        """
        return self.wait_get_element_text(self.user_name)

    def get_user_birthday(self):
        """
        获取用户生日
        :return: 用户生日
        """
        return self.wait_get_element_text(self.user_birthday)

    def get_user_phone(self):
        """
        获取用户手机号码
        :return: 手机号码
        """
        return self.wait_get_element_text(self.user_phone)

    def get_user_email(self):
        """
        获取用户邮箱
        :return: 用户邮箱
        """
        return self.wait_get_element_text(self.user_email)
