from Operating_UI_test.common.base_page import BasePage


class OperatingUserinfoUpdatePage(BasePage):
    """
    修改个人信息页
    """
    def update_username(self, name):
        """
        修改用户昵称
        :param name: 用户昵称
        :return: 修改用户昵称
        """
        return self.input_text(self.user_nickname, name)

    def update_user_realname(self, name):
        """
        修改用户真实姓名
        :param name: 用户真实姓名
        :return: 修改用户真实姓名
        """
        return self.input_text(self.user_realname, name)

    def update_user_sex_boy(self):
        """
        修改用户性别--男
        :return: 修改用户性别--男
        """
        return self.wait_click_element(self.user_sex_boy)

    def update_user_sex_girl(self):
        """
        修改用户性别--女
        :return: 修改用户性别--女
        """
        return self.wait_click_element(self.user_sex_girl)

    def update_user_birthday(self, birthday):
        """
        修改用户生日
        :param birthday: 生日格式 1995-10-11
        :return: 修改用户生日
        """
        return self.input_text(self.user_birthday, birthday)

    def update_user_phone(self, phone):
        """
        修改手机号码
        :param phone: 手机号码
        :return: 修改手机号码
        """
        return self.input_text(self.user_phone, phone)

    def update_user_email(self, email):
        """
        修改电子邮箱
        :param email: 电子邮箱
        :return: 修改电子邮箱
        """
        return self.input_text(self.user_email, email)

    def input_uld_pwd(self, uld_pwd):
        """
        输入旧密码
        :param uld_pwd: 旧密码
        :return: 旧密码
        """
        self.click_element(self.change_password_table)
        return self.input_text(self.uld_pwd, uld_pwd)

    def input_new_pwd(self, new_pwd):
        """
        输入新密码
        :param new_pwd: 新密码
        :return: 输入新密码
        """
        self.click_element(self.change_password_table)
        return self.input_text(self.new_pwd, new_pwd)

    def input_repeat_new_pwd(self, repeat_new_pwd):
        """
        确认新密码
        :param repeat_new_pwd: 确认新密码
        :return: 确认新密码
        """
        self.click_element(self.change_password_table)
        return self.input_text(self.repeat_new_pwd, repeat_new_pwd)

    def save(self):
        """
        保存
        :return: 保存
        """
        return self.click_element(self.confirm)

    def unsave(self):
        """
        取消
        :return: 取消
        """
        return self.wait_click_element(self.cancel)