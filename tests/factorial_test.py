import pytest
from application import factorial


def test_correct():
    assert factorial.factorial(5)==120


    
