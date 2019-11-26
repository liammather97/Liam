import pytest
from application import factorial


def correct_test():
    assert factorial(5)=="12"

def negative_test():
    assert factorial(-3)==""

def zero_test():
    assert factorial(0)==""

    
