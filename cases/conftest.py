import pytest
import requests

@pytest.fixture(name="common_session")
def common_session():
    s = requests.Session()
    yield  s
    s.close()