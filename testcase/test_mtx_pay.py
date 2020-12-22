# '''
#
# 前提：依赖于登录接口的
# 这里面写的都是关于下订单的所有场景的测试用例
# 1.先调用登录接口
# 2.然后再调用下订单的测试用例
# 宗旨：设计测试用例的时候，接口调用之间没有依赖关系（或者降到最低）
# 举例：存在依赖关系的接口，登录接口失败了并不会影响下订单接口
# '''
import requests

from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder
from api.apiPay import ApiPay


class TestPay:
    def setup_class(self):
        #创建session
        self.session=requests.session()

        #调用成功的登录接口
        ApiLogin().login_success(self.session)

        # 调用下订单接口
        ApiOrder().order(self.session)

        #创建支付对象
        self.pay_obj=ApiPay()




    def test_pay(self):
        '''
        测试用例
        :return:
        '''
        resp_pay=self.pay_obj.pay(self.session)
        #断言
        assert '支付成功' in resp_pay.text



