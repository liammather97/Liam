import pytest
import factorial


def correct_test():
    assert factorial.factorial(5)=="12"

def negative_test():
    assert factorial.factorial(-3)==""

def zero_test():
    assert factorial.factorial(0)==""

    
