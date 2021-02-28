import re
import copy

def extract_int(t):
    """extracts the value from a string param as int

    Args:
        t (string): parameter string to extract from

    Returns:
        int: value as an int
    """
    num_string = re.sub("\D", "", t) 
    return int(num_string)
    
class bedrooms_checker:
    """ checks and parses for number of bedrooms
    """
    property = 'bedrooms'
    
    def check(t):
        """checks if text contains bedroom parameter

        Args:
            t (string): string to check

        Returns:
            bool: if text matches bedroom parameter
        """
        return t.split(':')[0] == 'Number of Bedrooms'

    def parse(t):
        """parses bedrooms from string

        Args:
            t (string): string containing bedroom parameter

        Returns:
            int: number of bedrooms
        """
        return extract_int(t)


class bathrooms_checker:
    """checks and parses for number of bathrooms
    """
    property = 'bathrooms'

    def check(t):
        """checks if text contains bathroom parameter

        Args:
            t (string): string to check

        Returns:
            bool: if text matches parameter
        """
        return t.split(':')[0] == 'Number of Bathrooms'

    def parse(t):
        """parses number of bathrooms from string

        Args:
            t (string): string containing bathroom parameter

        Returns:
            int: number of bathrooms
        """
        return extract_int(t)

class flooring_checker:
    
    property = 'flooring_type'

    def check(t):
        return t.split(':')[0] == 'Flooring'

    def parse(t):
        return t.split(':')[1].strip() 


class garage_spaces_checker:
    
    property = 'garage_spaces'

    def check(t):
        return t.split(':')[0] == 'Number of Garage Spaces'
    
    def parse(t):
        return extract_int(t)


class days_on_market_checker:

    property = 'days_on_market'

    def check(t):
        return t.split(':')[0] == 'Days on Market'

    def parse(t):
        return extract_int(t)

class year_built_checker:

    property = 'year_built'

    def check(t):
        return t.split(':')[0] == 'Year Built'

    def parse(t):
        return extract_int(t)

class listing_status_checker:

    property = 'listing_status'

    def check(t):
        return t.split(':')[0] == 'Listing Status'

    def parse(t):
        return t.split(':')[1].strip()
class mls_status_checker:

    property = 'mls_status'

    def check(t):
        return t.split(':')[0] == 'MLS Status'

    def parse(t):
        return t.split(':')[1].strip()

class elementary_school_checker:

    property = 'elementary_school'

    def check(t):
        return t.split(':')[0] == 'Elementary School'

    def parse(t):
        return t.split(':')[1].strip()

class elementary_school_district_checker:

    property = 'elementary_school_district'

    def check(t):
        return t.split(':')[0] == 'Elementary School District'

    def parse(t):
        return t.split(':')[1].strip()

class high_school_checker:
    
    property = 'high_school_district'

    def check(t):
        return t.split(':')[0] == 'High School District'

    def parse(t):
        return t.split(':')[1].strip()

class mls_source_id_checker:

    property = 'mls_source_id'

    def check(t):
        return t.split(':')[0] == 'MLS/Source ID'

    def parse(t):
        return t.split(':')[1].strip()

class lot_area_checker:

    property = 'lot_area'

    def check(t):
        return t.split(':')[0] == 'Lot Area'

    def parse(t):
        string_num =  t.split(':')[1].strip().split(' ')[0]
        return float(string_num)

class lot_area_unit_checker:

    property = 'lot_area_unit'

    def check(t):
        return t.split(':')[0] == 'Lot Area'

    def parse(t):
        return t.split(':')[1].strip().split(' ')[1]

class jr_mid_school_checker:

    property = 'jr_mid_school'

    def check(t):
        return t.split(':')[0] == 'Jr High / Middle School'

    def parse(t):
        return t.split(':')[1].strip()

class jr_mid_school_district_checker:

    property = 'jr_mid_school_district'

    def check(t):
        return t.split(':')[0] == 'Jr High / Middle School District'
    
    def parse(t):
        return t.split(':')[1].strip()

class tax_amount_checker:

    property = 'tax_amount'

    def check(t):
        return t.split(':')[0] == 'Annual Tax Amount'

    def parse(t):
        string_num = t.split('$')[1].split(',')
        full_string = ''.join(string_num)
        return int(full_string)

category_checkers = [
    bedrooms_checker,
    bathrooms_checker,
    flooring_checker,
    garage_spaces_checker,
    days_on_market_checker,
    year_built_checker,
    listing_status_checker,
    mls_source_id_checker,
    elementary_school_checker,
    elementary_school_district_checker,
    high_school_checker,
    mls_source_id_checker,
    lot_area_checker,
    lot_area_unit_checker,
    jr_mid_school_checker,
    jr_mid_school_district_checker,
    tax_amount_checker
]

def parse_categories(category_parameters, category_checkers):
    result = {}
    checkers = copy.copy(category_checkers)
    params = copy.deepcopy(category_parameters)
    for p in params:
        for i, c in enumerate(checkers):
            if c.check(p):
                result[c.property] = c.parse(p)
                checkers.pop(i)
    return result

def parse_page_params(browser):
    # unpack listed price into a number
    listed_price = browser.find_by_xpath("//h3[@data-testid='on-market-price-details']")[0].value
    listed_price = listed_price.split('$')[1].split(',')
    listed_price = ''.join(listed_price)
    listed_price = int(listed_price)
    address_street = browser.find_by_xpath("//span[@data-testid='home-details-summary-headline']")[0].value
    address_city_state = browser.find_by_xpath("//span[@data-testid='home-details-summary-city-state']")[0].value
    return {
        'listed_price': listed_price,
        'address_street' : address_street,
        'address_city_state': address_city_state
    }

def transform_to_schema(dictionary, schema):
    l = {}
    for k in schema:
        if(k['name'] in dictionary):
            l[k['name']] = dictionary[k['name']]
        else:
            l[k['name']] = None
    return l

def parse_page(browser, schema, url):
    # 1. go to target page
    browser.visit(url)
    # 2. expand all amenities
    browser.find_by_xpath('//button[@data-testid="structured-amenities-table-see-all-button"]').click()
    # 3. instantiate the listing object
    listing = {
        'url': url
    }
    # 4. scrape page parameters
    page_params = parse_page_params(browser)
    listing.update(page_params)

    # 5. scrape structured categories
    structured_categories = browser.find_by_xpath('//div[@data-testid="structured-amenities-table-category"]')
    for c in structured_categories:
        category_parameters = c.find_by_tag('li')
        props = parse_categories(list(map(lambda x:x.text, category_parameters)), category_checkers)
        listing.update(props)

    return transform_to_schema(listing, schema)

def get_listing_urls_by_state_city(browser, state, city):
    url_root = 'https://www.trulia.com'

    url = url_root + '/' + state + '/' + city
    browser.visit(url)
    listings = browser.find_by_xpath('//a[@data-testid="home-marker"]')
    return list(map(lambda x: x['href'], listings))


def get_listings_by_state_city(browser, schema, state, city):

    listing_urls = get_listing_urls_by_state_city(browser, state, city)
    listing_urls = listing_urls[:10]

    home_data = []
    for url in listing_urls:
        data = parse_page(browser, schema, url)
        home_data.append(data)
    return home_data




    



