import pytest
import os
from common.read_yaml import get_yaml
import allure
import requests


class TestCeSuan():

    curpath = os.path.dirname(os.path.realpath(__file__))
    QiMingYuYue_yaml_file = os.path.join(curpath, "test_qimingyuyue.yml")
    test_QiMingYuYue_data = get_yaml(QiMingYuYue_yaml_file)


    @allure.story("事业详批-结果")
    def test_shiyexiangpi_result(self, s):
        '''测算-事业详批-结果'''
        url = "http://sandbox-cs.lingjm365.com/api/results/SYXP160794206600000090"
        r = s.get(url)
        print(r.text)
        assert r.json()["user_info"]["username"] == "测试"


    @allure.story("黄大仙-收费版-结果")
    def test_huangdaxian_result(self, s):
        '''测算-黄大仙-收费版-结果'''
        url = "http://sandbox-cs.lingjm365.com/api/results/HDXQ160799915400000060"
        r = s.get(url)
        print(r.text)
        assert r.json()["order_id"] == "HDXQ160799915400000060"
        assert r.json()["title"] == "第五十九签"


    @allure.story("新年套餐-八字合婚")
    def test_bazihehun_result(self, s):
        '''测算-新年套餐-八字合婚'''
        url ="http://sandbox-cs.lingjm365.com/api/results/BZHH160802184300000000"
        r = s.get(url)
        print(r.text)
        assert r.json()["male_self"]["solar_text"] == "1985年7月1日 时辰不清楚"
        assert r.json()["male_self"]["name"] == "测试"


    @allure.story("新年套餐-八字精批")
    def test_bazijingpi_result(self, s):
        '''测算-新年套餐-八字精批'''
        url = "http://sandbox-cs.lingjm365.com/api/results/JPPP160802279500000090"
        r = s.get(url)
        print(r.text)
        assert r.json()["pai_pan"]["wang_xiang_xiu_qiu_si"] == "火土木水金"
        assert r.json()["ming_pan_xing_xi_jie_du"]["title"] == "命盘信息解读"


    @allure.story("新年活动-八字姻缘")
    def test_baziyinyuan_result(self, s):
        '''测算-新年活动-八字姻缘'''
        url = "http://sandbox-cs.lingjm365.com/api/results/BZYY160802357400000060"
        r = s.get(url)
        print(r.text)
        assert r.json()["self"]["birthday"] == "1970-01-01"
        assert r.json()["self"]["username"] == "测试"


    @allure.story("新年活动-劫数")
    def test_jieshu_result(self, s):
        '''测算-新年活动-劫数'''
        url = "http://sandbox-cs.lingjm365.com/api/results/SNJS160802403500000000"
        r = s.get(url)
        print(r.text)
        assert r.json()["mingPan"]["name"] == "测试"
        assert r.json()["mingPan"]["gender"] == "男"


    @allure.story("新年活动-麦玲玲运程")
    def test_mailinglingyuncheng_result(self, s):
        '''测算-新年活动-麦玲玲运程'''
        url = "http://sandbox-cs.lingjm365.com/api/results/MNYC160802463200000010"
        r = s.get(url)
        print(r.text)
        assert r.json()["mai_ling_ling_pai_pan"]["sheng_xiao"] == "牛"


    @allure.story("新年活动-事业详批")
    def test_newshiyexiangpi_result(self, s):
        '''测算-新年活动-事业详批'''
        url = "http://sandbox-cs.lingjm365.com/api/results/SYXP160802516600000080"
        r = s.get(url)
        print(r.text)
        assert r.json()["user_info"]["username"] == "测试"
        assert r.json()["user_info"]["gender"] == "男"


    @allure.story("新年活动-一生财运")
    def test_yishengcaiyun_result(self, s):
        '''测算-新年活动-一生财运'''
        url = "http://sandbox-cs.lingjm365.com/api/results/YSCY160802559300000030"
        r = s.get(url)
        print(r.text)
        assert r.json()["caiFuGeJu"]["title"] == "你的先天财富格局"
        assert r.json()["caiFuGeJu"]["sub_title"] == "你的命局入铃陀格，财运格局较好，财星较旺，进财有方。"


    @allure.story("宋韶光")
    def test_songshaoguang_result(self, s):
        '''测算-宋韶光'''
        url = "http://sandbox-cs.lingjm365.com/api/results/SSXY160802589700000060"
        r = s.get(url)
        print(r.text)
        assert r.json()["liu_nian"]["title"] == "2021流年运程"
        print(r.text)


    @allure.story("姓名配对")
    def test_xingmingpeidui_result(self, s):
        '''测算-姓名配对'''
        url = "http://sandbox-cs.lingjm365.com/api/results/XMPD160802852300000080"
        r = s.get(url)
        print(r.text)
        assert r.json()["message"]["title"] == "你们合婚配对信息"
        assert r.json()["message"]["userInfo"]["info"][0]["name"] == "测试"


    @allure.story("pc起名-老师配置")
    def test_qiming_teacher_peizhi(self, s):
        '''测算-pc起名-老师配置'''
        url = "http://sandbox-cs.lingjm365.com/api/config/algorithm?product_id=pc_qiming"
        r = s.get(url)
        print(r.text)
        assert r.json()[0]["id"] == 1
        assert r.json()[0]["title"] == "李易玲助理门生起名"


    @allure.story("pc起名-预约")
    @pytest.mark.parametrize("test_input, expected", test_QiMingYuYue_data)
    def test_qiming_book(self, test_input, expected, s):
        '''测算-pc起名-预约'''
        url = "http://sandbox-cs.lingjm365.com/api/notify/book"
        r = s.post(url, data=test_input)
        print(r.text)
        if list(r.json().keys())[0] == "status":
            assert r.json()["status"] == expected["status"]
            assert r.json()["message"] == expected["message"]
        else:
            assert r.json()["code"] == expected["code"]
            assert r.json()["tips"] == expected["tips"]

    @allure.story("人工智能看缘分-结果接口")
    def test_rengongzhineng_result(self, s):
        '''测算-人工智能看缘分-结果接口'''
        url = "http://sandbox-cs.lingjm365.com/api/results/AIYF160820221200000010"
        r = s.get(url)
        print(r.text)
        assert r.json()["destiny"]["title"] == "缘分配对指数"
        assert r.json()["my_info"]["name"] == "测试"

    @allure.story("人工智能看缘分-支付页接口")
    def test_rengongzhineng_pay(self, s):
        '''测算-人工智能看缘分-支付页接口'''
        url = "http://sandbox-cs.lingjm365.com/api/results/user_info/AIYF160820221200000010"
        r = s.get(url)
        print(r.text)
        assert r.json()["destiny"]["title"] == "缘分配对指数"
        assert r.json()["my_info"]["name"] == "测试"


    # @allure.story("手相看姻缘")
    # def test_shouxiangkanyinyuan_result(self, s):
    #     '''测算-手相看姻缘'''
    #     url = "http://sandbox-cs.lingjm365.com/api/results/SXYY160826469100000040"
    #     r = s.get(url)
    #     print(r.text)
    #     assert r.json()["user_info"]["name"] == "测试"

    # @allure.story("手相看财运")
    # def test_shouxiangkancaiyun_result(self, s):
    #     '''测算-手相看财运'''
    #     url = "http://sandbox-cs.lingjm365.com/api/results/SXCY160826539700000070"
    #     r = s.get(url)
    #     print(r.text)
    #     assert r.json()["user_info"]["name"] == "测试"


    # @allure.story("手相看事业")
    # def test_shouxiangkanshiye_result(self, s):
    #     '''测算-手相看事业'''
    #     url = "http://sandbox-cs.lingjm365.com/api/results/SXSY160827197600000050"
    #     r = s.get(url)
    #     print(r.text)
    #     assert r.json()["user_info"]["name"] == "测试"


    @allure.story("塔罗-遇到另一半-支付页配置")
    def test_yudaolingyiban_pay(self, s):
        '''测算-塔罗-遇到另一半-支付页配置'''
        url = "http://sandbox-cs.lingjm365.com/api/config/pay/WLTH160827220500000040"
        r = s.get(url)
        print(r.text)
        assert r.json()["order_id"] == "WLTH160827220500000040"
        assert r.json()["status"] == "paid"


    @allure.story("塔罗-遇到另一半-结果")
    def test_yudaolingyiban_result(self, s):
        '''测算-塔罗-遇到另一半-结果'''
        url = "http://sandbox-cs.lingjm365.com/api/results/WLTH160827220500000040"
        r = s.get(url)
        print(r.text)
        assert r.json()["analyses"][0]["title"] == "你目前的感情狀態？"
        assert r.json()["analyses"][0]["tarotCard"]["id"] == 23


    @allure.story("AI前世姻缘")
    def test_AIqianshiyiyuan_result(self, s):
        '''测算-AI前世姻缘'''
        url = "http://sandbox-cs.lingjm365.com/api/results/AIQY160827355200000030"
        r = s.get(url)
        print(r.text)
        assert r.json()["yinYuan"]["title"] == "你們的前世基因牽絆"
        assert r.json()["yinYuan"]["male"]["name"] == "测试"


    @allure.story("八字合婚书")
    def test_bazihehunshu_result(self, s):
        '''测算-八字合婚书'''
        url = "http://sandbox-cs.lingjm365.com/api/results/BZHS161017938500000070"
        r = s.get(url)
        print(r.text)
        assert r.json()["male_self"]["name"] == "测试"
        assert r.json()["female_self"]["name"] == "测试"


    @allure.story("每日运势-结果页")
    def test_meiriyunshi_result(self, s):
        '''测算-每日运势-结果页'''
        url = "http://sandbox-cs.lingjm365.com/api/results/MRYS156816768309500070"
        r = s.get(url)
        print(r.text)
        assert r.json()["today"]["labels"][0]["value"] == "23"
        assert r.json()["today"]["labels"][0]["active"] == False


    @allure.story("恋爱配对2020版-结果")
    def test_lianaipeidui_result(self, s):
        '''测算-恋爱配对2020版-结果'''
        url = "http://sandbox-cs.lingjm365.com/api/results/LAPD160827448400000050"
        r = s.get(url)
        print(r.text)
        assert r.json()["couples_info"]["self"]["name"] == "测试"
        assert r.json()["couples_info"]["self"]["birth_time"] == "1985年07月01日 时辰不清楚"


    @allure.story("明日运势-结果")
    def test_mingriyunshi_result(self, s):
        '''测算-明日运势-结果'''
        url = "http://sandbox-cs.lingjm365.com/api/results/MRYS160827626100000070"
        r = s.get(url)
        print(r.text)
        assert r.json()["self"]["username"] == "测试"
        assert r.json()["self"]["gender"] == "男"


    @allure.story("奇门遁甲")
    def test_qimendunjia_result(self, s):
        '''测算-奇门遁甲'''
        url = "http://sandbox-cs.lingjm365.com/api/results/QMDJ160828075200000060"
        r = s.get(url)
        print(r.text)
        assert r.json()["jianJie"]["title"] == "奇门遁甲简介"


    # @allure.story("星座月运势-支付页")
    # def test_xingzuoyueyunshi_pay(self, s):
    #     '''测算-星座月运势-支付页'''
    #     url = "http://sandbox-cs.lingjm365.com/api/results/detain/JPXZ160828104200000050"
    #     r = s.get(url)
    #     print(r.text)
    #     assert r.json()["svg_points"][0]["title"] == "现代星盘"
    #     assert r.json()["year"] == "2021"


    @allure.story("星座月运势-套餐内容")
    def test_xingzuoyueyunshi_taocan(self, s):
        '''测算-星座月运势-套餐内容'''
        url = "http://sandbox-cs.lingjm365.com/api/config/index/mei_yue_yun_shi"
        r = s.get(url)
        print(r.text)
        assert r.json()["packages"][0]["title"] == "本月运势详批"
        assert r.json()["packages"][0]["package"] == 1


    @allure.story("观音灵签-随机签")
    def test_guanyinlingqian_suiji(self, s):
        '''测算-观音灵签-随机签'''
        url = "http://sandbox-cs.lingjm365.com/api/config/algorithm?product_id=guan_yin_ling_qian"
        r = s.get(url)
        print(r.text)
        assert type(r.json()["number"]) == int
        assert type(r.json()["num"]) == str


    @allure.story("观音灵签-大师版")
    def test_guanyinlingqian_result(self, s):
        '''测算-观音灵签-大师版'''
        url = "http://sandbox-cs.lingjm365.com/api/results/LQYY160828798000000050"
        r = s.get(url)
        print(r.text)
        assert r.json()["signInfo"]["title"] == "靈簽信息"
        assert r.json()["content"]["title"] == "觀音靈簽"



























