from scripts.trulia_scraper import *


# Interior Features

def test_bedroom_checker():
    test_string = "Number of Bedrooms: 4"

    assert bedrooms_checker.check(test_string) == True

    assert bedrooms_checker.parse(test_string) == 4

def test_bathroom_checker():
    test_string = "Number of Bathrooms: 2"

    assert bathrooms_checker.check(test_string) == True
    
    assert bathrooms_checker.parse(test_string) == 2
    
def test_full_bathroom_checker():
    test_string = "Number of Bathrooms (full): 2"

    assert full_bathrooms_checker.check(test_string) == True
    
    assert full_bathrooms_checker.parse(test_string) == 2

def test_flooring_checker():
    test_string = "Flooring: Hardwood"

    assert flooring_checker.check(test_string) == True

    assert flooring_checker.parse(test_string) == "Hardwood"

# Exterior Features

def test_garage_spaces_checker():
    test_string = "Number of Garage Spaces: 1"

    assert garage_spaces_checker.check(test_string) == True

    assert garage_spaces_checker.parse(test_string) == 1

def test_parking_features_checker():
    test_string = "Parking: Private,Detached"
    
    assert parking_features_checker.check(test_string) == True

    assert parking_features_checker.parse(test_string) == 'Private,Detached'

# Days on Market

def test_days_on_market_checker():    
    test_string = "Days on Market: 4"

    assert days_on_market_checker.check(test_string) == True

    assert days_on_market_checker.parse(test_string) == 4

# Property Information

def test_year_built_checker():
    test_string = "Year Built: 1954"

    assert year_built_checker.check(test_string) == True

    assert year_built_checker.parse(test_string) == 1954

def test_property_type_checker():

    test_string = "Property Type: Residential"

    assert property_type_checker.check(test_string) == True

    assert property_type_checker.parse(test_string) == 'Residential'

def test_property_subtype_checker():
    
    test_string = "Property Subtype: Single Family Residence"
    
    assert property_subtype_checker.check(test_string) == True
    
    assert property_subtype_checker.parse(test_string) == 'Single Family Residence'

def test_architecture_style_checker():
    test_string = "Architecture: Colonial"

    assert architecture_style_checker.check(test_string) == True

    assert architecture_style_checker.parse(test_string) == 'Colonial'

# Active Status

def test_listing_status_checker():
    test_string = "Listing Status: Active"

    assert listing_status_checker.check(test_string) == True
    
    assert listing_status_checker.parse(test_string) == "Active"

def test_mls_status_checker():
    test_string = "MLS Status: A"

    assert mls_status_checker.check(test_string) == True

    assert mls_status_checker.parse(test_string) == "A"

# Location

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

    assert jr_mid_school_checker.parse(test_string) == "Hicksville Middle School"

def test_jr_mid_school_district_checker():
    test_string = "Jr High / Middle School District: Hicksville"

    assert jr_mid_school_district_checker.check(test_string) == True

    assert jr_mid_school_district_checker.parse(test_string) == "Hicksville"

def test_high_school_checker():
    test_string = "High School District: Hicksville"

    assert high_school_checker.check(test_string) == True

    assert high_school_checker.parse(test_string) == "Hicksville"

# Agent Information

def test_mls_source_id_checker():
    test_string = "MLS/Source ID: 3287583"

    assert mls_source_id_checker.check(test_string) == True

    assert mls_source_id_checker.parse(test_string) == "3287583"

# Building

def test_building_area_unit_checker():
    test_string = "Building Area Units: Square Feet"

    assert building_area_unit_checker.check(test_string) == True

    assert building_area_unit_checker.parse(test_string) == "Square Feet"

# lot information

def test_lot_area_checker():
    test_string = "Lot Area: 0.14 Acres"

    assert lot_area_checker.check(test_string) == True

    assert lot_area_checker.parse(test_string) == 0.14
    
    assert lot_area_unit_checker.check(test_string) == True

    assert lot_area_unit_checker.parse(test_string) == "Acres"

# tax information

def test_tax_amount_checker():
    test_string = "Annual Tax Amount: $8,479"

    assert tax_amount_checker.check(test_string) == True

    assert tax_amount_checker.parse(test_string) == 8479


def test_tax_block_checker():
    test_string = "Tax Block: 270"

    assert tax_block_checker.check(test_string) == True
    
    assert tax_block_checker.parse(test_string) == '270'


def test_tax_lot_checker():
    test_string = "Tax Lot: 47"

    assert tax_lot_checker.check(test_string) == True
    
    assert tax_lot_checker.parse(test_string) == '47'

def text_tax_map_number():
    test_string = "Tax Map Number: N2489-46-270-00-0047-0"

    assert tax_map_num_checker.check(test_string) == True

    assert tax_map_num_checker.parse(test_string) == 'N2489-46-270-00-0047-0'
