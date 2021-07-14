import pytest
import os
import allure
from common.read_yaml import get_yaml


class TestXiaoChengXu():

    def test_get_userinfo(self, s):
        '''获取用户信息'''
        url = "http://sandbox-cs.lingjm365.com/api/wechat/getuserinfo"
        body = {
            "wx": 99,
            "code": 1
        }
        r = s.get(url, params=body)
        print(r.text)


    def test_wechat_poor(self, s):
        '''微信池'''
        url = "http://sandbox-cs.lingjm365.com/api/wechat/pool"
        body = {
            "group": "pc_qiming"
        }
        r = s.get(url, params=body)
        assert r.json()["id"] == "66"
        assert r.json()["wechat_id"] == "duan9465"


    def test_toutiao_neirong(self, s):
        '''头条-内容检测'''
        url = "http://sandbox-cs.lingjm365.com/api/toutiao/text/antidirt"
        body = {
            "content[]": "我爱中国"
        }
        r = s.post(url, params=body)
        assert r.json()["data"][0]["code"] == 0


    # def test_erweima(self, s):
    #     '''生成二维码'''
    #     url = "http://sandbox-cs.lingjm365.com/api/toutiao/qrcode"
    #     body = {
    #         "program_alias": "ge_ren_qing_gan",
    #         "path": "xxx/index?channel=test",
    #         "appname": "toutiao"
    #     }
    #     r = s.post(url, params=body)
    #     assert r.json()["url"] == "https://stest.ggwan.com/image/dashuju-oss/a7a1a17bd51f0e-320x320.jpg"
    #     assert r.json()["res_id"] == "1e0ee0b14152f951ff00020e0fab75b4"

