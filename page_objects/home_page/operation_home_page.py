# 运营端首页
from Operating_UI_test.common.base_page import BasePage
from Operating_UI_test.utils.all_path import operating_elements_yaml_path
from Operating_UI_test.page_objects.user_manage.user_info_page.operation_register_user_page import OperatingRegisterUserPage
from Operating_UI_test.page_objects.user_manage.user_info_page.text_message_user_page import OperatingTextMessageUserPage
from Operating_UI_test.page_objects.user_manage.user_info_page.unipay_user_page import OperatingUnionPayUserPage
from Operating_UI_test.page_objects.user_manage.user_info_page.wx_user_page import OperatingWXUserPage
from Operating_UI_test.page_objects.user_manage.user_info_page.ABCbank_user_page import OperatingABCUserPage
from Operating_UI_test.page_objects.user_manage.address_page.address_page import OperatingAddressPage
from Operating_UI_test.page_objects.user_manage.authorization_info.activity_authorization_page import OperatingActivityAuthorizationPage
from Operating_UI_test.page_objects.user_manage.authorization_info.login_authorization_page import OperatingLoginAuthorizationPage
from Operating_UI_test.page_objects.user_manage.user_order.user_fill_continuously_order_page import OperatingUserFillContinuouslyOrderPage
from Operating_UI_test.page_objects.user_manage.user_order.coupon_order_page import OperatingCouponOrderPage
from Operating_UI_test.page_objects.user_manage.user_coupon.coupon_use_record_page import OperatingCouponUserRecordPage
from Operating_UI_test.page_objects.user_manage.user_coupon.coupon_collection_record_page import OperatingCouponCollectionRecordPage
from Operating_UI_test.page_objects.user_manage.user_car.user_car_page import OperatingUserCarPage


class OperatingHomePage(BasePage):
    """
    运营端首页中进入各个页面。
    """
    def logout(self):
        """
        退出登录
        :return:
        """
        self.click_element(self.items().user_img)
        self.click_element(self.logout_button)
        self.click_element(self.logout_confirm)

    def user_info(self):
        """
        个人信息展示页
        :return:
        """
        self.click_element(self.user_img)

    def register_user(self):
        """
        进入用户管理 ==> 用户信息 ==> 注册用户页
        :return:
        """
        if self.isexist_element(self.register_user_page, Action='注册用户页'):
            self.click_element(self.register_user_page)
        else:
            self.click_element(self.user_manage)
            self.click_element(self.userinfo)
            self.click_element(self.register_user_page)
        return OperatingRegisterUserPage(operating_elements_yaml_path)

    def text_message_user(self):
        """
        进入用户管理 ==> 用户信息 ==> 短信用户页
        :return:
        """
        if self.isexist_element(self.text_message_user_page, Action='短信用户页'):
            self.click_element(self.text_message_user_page)
        else:
            self.click_element(self.user_manage)
            self.click_element(self.userinfo)
            self.click_element(self.text_message_user_page)
        return OperatingTextMessageUserPage(operating_elements_yaml_path)

    def wx_user_page(self):
        """
        进入用户管理 ==> 用户信息 ==> 微信用户页
        :return:
        """
        if self.isexist_element(self.WX_user_page, Action='微信用户页'):
            self.click_element(self.WX_user_page)
        else:
            self.click_element(self.user_manage)
            self.click_element(self.userinfo)
            self.click_element(self.WX_user_page)
        return OperatingWXUserPage(operating_elements_yaml_path)

    def abcbank_user_page(self):
        """
        进入用户管理 ==> 用户信息 ==> 农行用户页
        :return:
        """
        if self.isexist_element(self.ABC_user_page, Action='农行用户页'):
            self.click_element(self.ABC_user_page)
        else:
            self.click_element(self.user_manage)
            self.click_element(self.userinfo)
            self.click_element(self.ABC_user_page)
        return OperatingABCUserPage(operating_elements_yaml_path)

    def unionpay_user_page(self):
        """
        进入用户管理 ==> 用户信息 ==> 云闪付用户页
        :return:
        """
        if self.isexist_element(self.UnionPay_user_page, Action='云闪付用户页'):
            self.click_element(self.UnionPay_user_page)
        else:
            self.click_element(self.user_manage)
            self.click_element(self.userinfo)
            self.click_element(self.UnionPay_user_page)
        return OperatingUnionPayUserPage(operating_elements_yaml_path)

    def address(self):
        """
        进入用户管理 ==> 收货地址页
        :return:
        """
        if self.isexist_element(self.address_page, Action='收货地址页'):
            self.click_element(self.address_page)
        return OperatingAddressPage(operating_elements_yaml_path)

    def login_authorization_page(self):
        """
        进入用户管理 ==> 授权信息 ==> 登录授权
        :return:
        """
        if self.isexist_element(self.login_authorization, Action='登录授权页'):
            self.click_element(self.login_authorization)
        else:
            self.click_element(self.authorization_info)
            self.click_element(self.login_authorization)
        return OperatingLoginAuthorizationPage(operating_elements_yaml_path)

    def activity_authorization_page(self):
        """
        进入用户管理 ==> 授权信息 ==> 活动授权
        :return:
        """
        if self.isexist_element(self.activity_authorization, Action='活动授权页'):
            self.click_element(self.activity_authorization)
        else:
            self.click_element(self.authorization_info)
            self.click_element(self.activity_authorization)
        return OperatingActivityAuthorizationPage(operating_elements_yaml_path)

    def user_fill_continuously_order_page(self):
        """
        用户管理 ==> 用户订单 ==> 直充权益订单
        :return:
        """
        if self.isexist_element(self.user_fill_continuously_order, Action='直充权益订单页'):
            self.click_element(self.user_fill_continuously_order)
        else:
            self.click_element(self.user_order)
            self.click_element(self.user_fill_continuously_order)
        return OperatingUserFillContinuouslyOrderPage(operating_elements_yaml_path)

    def coupon_order_page(self):
        """
        用户管理 ==> 用户订单 ==> 优惠券订单
        :return:
        """
        if self.isexist_element(self.coupon_order, Action='优惠券订单页'):
            self.click_element(self.coupon_order)
        else:
            self.click_element(self.user_order)
            self.click_element(self.coupon_order)
        return OperatingCouponOrderPage(operating_elements_yaml_path)

    def coupon_collection_record_page(self):
        """
        用户管理 ==> 用户优惠券 ==> 优惠券领取记录
        :return:
        """
        if self.isexist_element(self.coupon_collection_record, Action='优惠券领取记录页'):
            self.click_element(self.coupon_collection_record)
        else:
            self.click_element(self.user_coupon)
            self.click_element(self.coupon_collection_record)
        return OperatingCouponCollectionRecordPage(operating_elements_yaml_path)

    def coupon_use_record_page(self):
        """
        用户管理 ==> 用户优惠券 ==> 优惠券使用记录
        :return:
        """
        if self.isexist_element(self.coupon_use_record, Action='优惠券使用记录页'):
            self.click_element(self.coupon_use_record)
        else:
            self.click_element(self.user_coupon)
            self.click_element(self.coupon_use_record)
        return OperatingCouponUserRecordPage(operating_elements_yaml_path)

    def user_car_page(self):
        """
        用户管理 ==> 用户车辆
        :return:
        """
        if self.isexist_element(self.user_car, Action='用户车辆页'):
            self.click_element(self.user_car)
        return OperatingUserCarPage(operating_elements_yaml_path)