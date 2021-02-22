from scripts.category_parser import *


def test_bedroom_parser():
    test_string = "Number of Bedrooms: 4"

    assert bedrooms_checker.check(test_string) == True

    assert bedrooms_checker.parse(test_string) == 4

def test_bathroom_parser():
    test_string = "Number of Bathrooms: 2"

    assert bathrooms_checker.check(test_string) == True
    
    assert bathrooms_checker.parse(test_string) == 2