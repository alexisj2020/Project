import pytest
from DataReorganization import *

@pytest.mark.parametrize("dataset,expected",
                         [(list(range(1,144)), [6.5,18.5,30.5,42.5,54.5,66.5,78.5,90.5,102.5,114.5,126.5]),
                          (list(range(1,65)),[6.5,18.5,30.5,42.5,54.5])
                          ])

def test_annual(dataset,expected):
    observed=annual(dataset)
    assert observed==expected
    return NotImplementedError