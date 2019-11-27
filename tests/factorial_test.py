import pytest
from application import factorial


def test_correct():
    assert factorial.factorial(5)==120

def test_big():
    assert factorial.factorial(13)==6227020800

def test_bigger():
    assert factorial.factorial(20)==2432902008176640000

def test_evenbigger():
    assert factorial.factorial(25)==15511210043330985984000000


    
