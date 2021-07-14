import pytest
import os
import allure
from common.read_yaml import get_yaml


class TestGongGongFenLei():


    curpath = os.path.dirname(os.path.realpath(__file__))
    ShenQingPingLun_yaml_file = os.path.join(curpath, "test_shenqingpinglun.yml")
    test_ShenQingPingLun_data = get_yaml(ShenQingPingLun_yaml_file)
    PingLunChaXun_yaml_file = os.path.join(curpath, "test_pinglunchaxun.yml")
    test_PingLunChaXun_data = get_yaml(PingLunChaXun_yaml_file)
    ZiYuanShuJu_yaml_file = os.path.join(curpath, "test_get_ziyuanshuju.yml")
    test_Get_ZiYuanShuJu_data = get_yaml(ZiYuanShuJu_yaml_file)

    # @allure.story("申请评论")
    # @pytest.mark.parametrize("test_input, expected", test_ShenQingPingLun_data)
    # def test_ShenQingPingLun(self, test_input, expected, s):
    #     '''申请评论'''
    #     url = "http://sandbox-cs.lingjm365.com/api/comments/accuracy"
    #     r = s.post(url,data=test_input)
    #     print(r.text)
    #     assert r.json()["code"] == expected["code"]
    #     assert r.json()["msg"] == expected["msg"]

    @allure.story("app配置接口")
    def test_app_peizhijiekou(self, s):
        '''app配置接口'''
        url = "http://sandbox-cs.lingjm365.com/api/config/appconfig"
        body = {
            "channel": "app_ios_1460957091"
        }
        r = s.get(url, params=body)
        print(r.text)
        assert r.json()["navigatorData"][0]["title"] == "塔罗咨询"
        print(r.text)


    @allure.story("融合站点列")
    def test_ronghezhandian_list(self, s):
        '''融合站点列'''
        url = "http://sandbox-cs.lingji333.cn/api/products/site"
        r = s.get(url)
        print(r.text)
        assert r.json()[0]["name"] == "【2021年最新版】精品紫微财运"


    @allure.story("评论查询")
    @pytest.mark.parametrize("test_input, expected", test_PingLunChaXun_data)
    def test_pinglunchaxun(self, test_input, expected, s):
        '''评论查询'''
        url = "http://sandbox-cs.lingjm365.com/api/comments/accuracy"
        r = s.get(url, params=test_input)
        print(r.text)
        assert r.json()["code"] == expected["code"]
        print(r.text)

    # def test_get_id_order():
    #     '''获取openid订单'''
    #     url = "http://sandbox-cs.lingjm365.com/api/distribution/openid"

    @allure.story("获取微信订单名字")
    def test_get_wechat_name(self, s):
        '''获取微信订单名字'''
        url = "http://sandbox-cs.lingjm365.com/api/distribution/names"
        body = {
            "product_id": "kan_yuan_fen"
        }
        r = s.get(url, params=body)
        print(r.text)
        assert r.json()[0]["nickname"] == "小灵"
        print(r.text)


    @allure.story("首次免单")
    def test_free_first(self, s):
        '''首次免单'''
        url = "http://sandbox-cs.lingjm365.com/api//distribution/first"
        body = {
            "order_id": "BDXM160707737600000000",
            "product_id": "shou_xiang_yan_jiu_yuan"
        }
        r = s.post(url, params=body)
        print(r.text)
        assert r.json()["code"] == 20005

    # def test_paihangban():
    #     '''排行榜'''
    #     url = "http://sandbox-cs.lingjm365.com/api//distribution/rank"
    #     body = {
    #         "openid": "",
    #         "product_id": ""
    #     }

    @allure.story("支付挽留")
    def test_pay_wanliu(self, s):
        '''支付挽留'''
        url = "http://sandbox-cs.lingjm365.com/api/results/detain/{order_id}"
        body = {
            "order_id": "BDXM160707737600000000"
        }
        r = s.get(url, params=body)
        print(r.text)
        print(r.text)

    @allure.story("保存投诉")
    def test_baocuntousu(self, s):
        '''保存投诉'''
        url = "http://sandbox-cs.lingjm365.com/api/complain"
        body = {
            "product_id": "da_shi_yun_cheng_he_ji",
            "content": "测试投诉",
            "phone": 13750038037
        }
        r = s.post(url, data=body)
        print(r.text)
        assert r.json()["status"] == 200
        assert r.json()["msg"] == "success"

    # def test_upload_image():
    #     '''上传图片'''
    #     url = "http://sandbox-cs.lingjm365.com/api/tools/images"
    #     body = {
    #         "image": "B34uSEBSToGj2FA-c4Jg0j5nlaB67NMvgdDJqqglv-ZmyNfGhm5sEON1dJpPqqev",
    #         "type": "jpg"
    #     }

    @allure.story("退款回调接口")
    def test_tuikuan(self, s):
        '''退款回调接口'''
        url = "http://sandbox-cs.lingjm365.com/api/payments/refund"
        body = {
            "order_id": "BDXM160707737600000000"
        }
        r = s.post(url, data=body)
        print(r.text)
        assert r.text == "success"
    #
    # def test_shouyepeizhi():
    #     '''首页配置'''
    #     url = "http://sandbox-cs.lingjm365.com/api/config/index/{product_id}"

    @allure.story("获取资源数据")
    @pytest.mark.parametrize("test_input, expected", test_Get_ZiYuanShuJu_data)
    def test_get_ziyuanshuju(self, test_input, expected, s,):
        '''获取资源数据'''
        url = "http://sandbox-cs.lingjm365.com/api/resource/show"
        r = s.get(url, params=test_input)
        print(r.text)
        if list(r.json().keys())[0] == "cs_list":
            assert r.json()["cs_list"][0]["name"] == expected["name"]
            assert r.json()["cs_list"][0]["desc"] == expected["desc"]
        else:
            assert r.json()["code"] == expected["code"]
            assert r.json()["tips"] == expected["tips"]










