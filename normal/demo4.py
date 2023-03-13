import pytest

def find_sum(l):
    s=0
    for i in range(l):
        s+=i
    return s
@pytest.mark.parametrize("l,exp_output",[([10,20])
def test_sum(l,expp_output):
    assert list_sum(l)==exp_output

