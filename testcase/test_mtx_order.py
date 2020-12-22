'''

前提：依赖于登录接口的
这里面写的都是关于下订单的所有场景的测试用例
1.先调用登录接口
2.然后再调用下订单的测试用例
宗旨：设计测试用例的时候，接口调用之间没有依赖关系（或者降到最低）
举例：存在依赖关系的接口，登录接口失败了并不会影响下订单接口
'''
import requests

from api.apiLogin import ApiLogin
from api.apiOrder import ApiOrder


class TestOrder:
    def setup_class(self):
        self.session=requests.session()
        #创建order对象
        self.order_obj=ApiOrder()
        #调用成功的登录接口
        ApiLogin().login_success(self.session)



    def test_order(self):
        '''
        测试用例
        :return:
        '''
        resp_order=self.order_obj.order(self.session)
        #断言
        assert resp_order.json().get('msg')=='提交成功'

