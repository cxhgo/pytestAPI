import requests
import pytest
from common.dingding_robot import dingding


@pytest.fixture(scope="session", name="s")
def get_session():
    s = requests.Session()
    yield s


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )
    # 添加参数到pytest.ini
    parser.addini('url', type=None, default="http://sandbox-cs.lingjm365.com", help='添加 url 访问地址参数')


@pytest.fixture(scope="session")
def home_url(pytestconfig):
    url = pytestconfig.getini('base_url')
    print("\n读取到配置文件的url地址：%s" % url)
    return url


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # print('------------------------------------')

    # 获取钩子方法的调用结果
    out = yield
    # print('用例执行结果', out)

    # 3. 从钩子方法的调用结果中获取测试报告
    report = out.get_result()

    # print('测试报告：%s' % report)
    # print('步骤：%s' % report.when)
    # print('nodeid：%s' % report.nodeid)
    # print('description:%s' % str(item.function.__doc__))
    # print(('运行结果: %s' % report.outcome))
    if report.outcome == "failed":
        dingding(str(item.function.__doc__))

