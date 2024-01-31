# 验证每个页面都能正常加载的用例
from Operating_UI_test.utils.all_path import operating_elements_yaml_path
from Operating_UI_test.page_objects.login_page.operation_login import OperatingLoginPage


class EachPageLoadsNormally:
    def user_manage_page(self):
        # 登录
        login = OperatingLoginPage(operating_elements_yaml_path).open_login_page().login_sys()
        # 验证用户管理 ==> 用户信息 ==> 注册用户页是否正常加载数据
        login.register_user().is_have_msg()
        # 验证用户管理 ==> 用户信息 ==> 短信用户页是否正常加载数据
        login.text_message_user().is_have_msg()
        # 验证用户管理 ==> 用户信息 ==> 微信用户页是否正常加载数据
        login.wx_user_page().is_have_msg()
        # 验证用户管理 ==> 用户信息 ==> 农行用户页是否正常加载数据
        login.abcbank_user_page().is_have_msg()
        # 验证用户管理 ==> 用户信息 ==> 云闪付用户页是否正常加载数据
        login.unionpay_user_page().is_have_msg()
        # 验证用户管理 ==> 收货地址页是否正常加载数据
        login.address().is_have_msg()
        # 验证用户管理 ==> 授权信息 ==> 登录授权页是否正常加载数据
        login.login_authorization_page().is_have_msg()
        # 验证用户管理 ==> 授权信息 ==> 活动授权页是否正常加载数据
        login.activity_authorization_page().is_have_msg()
        # 验证用户管理 ==> 用户订单 ==> 直充权益订单页是否正常加载数据
        login.user_fill_continuously_order_page().is_have_msg()
        # 验证用户管理 ==> 用户订单 ==> 优惠券订单页是否正常加载数据
        login.coupon_order_page().is_have_msg()
        # 验证用户管理 ==> 用户优惠券 ==> 优惠券领取记录页是否正常加载数据
        login.coupon_collection_record_page().is_have_msg()
        # 验证用户管理 ==> 用户优惠券 ==> 优惠券使用记录页是否正常加载数据
        login.coupon_use_record_page().is_have_msg()
        # 验证用户管理 ==> 用户车辆页是否正常加载数据
        login.user_car_page().is_have_msg()
        return print('验证运营端用户管理页每个页面都能正常加载的用例执行完成。')

    def product_manage_page(self):



if __name__ == '__main__':
    EachPageLoadsNormally().user_manage_page()