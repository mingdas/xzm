import pytest
@pytest.fixture(params=["参数1","参数2"])
def myfixture(request):
    print("\n执行myfixture, 带参数%s" % request.param)