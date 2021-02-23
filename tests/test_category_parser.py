from scripts.category_parser import *


def test_bedroom_checker():
    test_string = "Number of Bedrooms: 4"

    assert bedrooms_checker.check(test_string) == True

    assert bedrooms_checker.parse(test_string) == 4

def test_bathroom_checker():
    test_string = "Number of Bathrooms: 2"

    assert bathrooms_checker.check(test_string) == True
    
    assert bathrooms_checker.parse(test_string) == 2

def test_flooring_checker():
    test_string = "Flooring: Hardwood"

    assert flooring_checker.check(test_string) == True

    assert flooring_checker.parse(test_string) == "Hardwood"

def test_garage_spaces_checker():
    test_string = "Number of Garage Spaces: 1"

    assert garage_spaces_checker.check(test_string) == True

    assert garage_spaces_checker.parse(test_string) == 1

def test_days_on_market_checker():    
    test_string = "Days on Market: 4"

    assert days_on_market_checker.check(test_string) == True

    assert days_on_market_checker.parse(test_string) == 4

def test_year_built_checker():
    test_string = "Year Built: 1954"

    assert year_built_checker.check(test_string) == True

    assert year_built_checker.parse(test_string) == 1954

def test_listing_status_checker():
    test_string = "Listing Status: Active"

    assert listing_status_checker.check(test_string) == True
    
    assert listing_status_checker.parse(test_string) == "Active"

def test_mls_status_checker():
    test_string = "MLS Status: A"

    assert mls_status_checker.check(test_string) == True

    assert mls_status_checker.parse(test_string) == "A"

def test_elementary_school_checker():
    test_string = "Elementary School: Dutch Lane School"

    assert elementary_school_checker.check(test_string) == True

    assert elementary_school_checker.parse(test_string) == "Dutch Lane School"

def test_elementary_school_district_checker():
    test_string = "Elementary School District: Hicksville"

    assert elementary_school_district_checker.check(test_string) == True

    assert elementary_school_district_checker.parse(test_string) == "Hicksville"

def test_jr_mid_school_checker():
    test_string = "Jr High / Middle School: Hicksville Middle School"

    assert jr_mid_school_checker.check(test_string) == True

    assert jr_mid_school_checker.parse(test_string) == "Jr High / Middle School: Hicksville Middle School"

def test_jr_mid_school_district_checker():
    test_string = "Jr High / Middle School District: Hicksville"

    assert jr_mid_school_district_checker.check(test_string) == True

    assert jr_mid_school_district_checker.parse(test_string) == "Hicksville"

def test_high_school_checker():
    test_string = "High School District: Hicksville"

    assert high_school_checker.check(test_string) == True

    assert high_school_checker.parse(test_string) == "Hicksville"

def test_mls_source_id_checker():
    test_string = "MLS/Source ID: 3287583"

    assert mls_source_id_checker.check(test_string) == True

    assert mls_source_id_checker.parse(test_string) == "3287583"

def test_lot_area_checker():
    test_string = "Lot Area: 0.14 Acres"

    assert lot_area_checker.check(test_string) == True

    assert lot_area_checker.parse(test_string) == 0.14
    
    assert lot_area_unit_checker.check(test_string) == True

    assert lot_area_unit_checker.parse(test_string) == "Acres"

def test_tax_amount_checker():
    test_string = "Annual Tax Amount: $8,479"

    assert tax_amount_checker.check(test_string) == True

    assert tax_amount_checker.parse(test_string) == 8479



