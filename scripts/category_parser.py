
def extract_int(t):
    """extracts the value from a string param as int

    Args:
        t (string): parameter string to extract from

    Returns:
        int: value as an int
    """
    num_string = t.split(':')[1].strip()
    return int(num_string)
    
class bedrooms_checker:
    """ checks and parses for number of bedrooms
    """
    
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

    def check(t):
        return t.split(':')[0] == 'Flooring'

    def parse(t):
        return t.split(':')[1].strip() 


class garage_spaces_checker:

    def check(t):
        return t.split(':')[0] == 'Number of Garage Spaces'
    
    def parse(t):
        return extract_int(t)


class days_on_market_checker:

    def check(t):
        return t.split(':')[0] == 'Days on Market'

    def parse(t):
        return extract_int(t)

class year_built_checker:

    def check(t):
        return t.split(':')[0] == 'Year Built'

    def parse(t):
        return extract_int(t)

class listing_status_checker:

    def check(t):
        return t.split(':')[0] == 'Listing Status'

    def parse(t):
        return t.split(':')[1].strip()

class elementary_school_checker:

    def check(t):
        return t.split(':')[0] == 'Elementary School'

    def parse(t):
        return t.split(':')[1].strip()
    
class mls_status_checker:

    def check(t):
        return t.split(':')[0] == 'MLS Status'

    def parse(t):
        return t.split(':')[1].strip()

class elementary_school_district_checker:

    def check(t):
        return t.split(':')[0] == 'Elementary School District'

    def parse(t):
        return t.split(':')[1].strip()

class high_school_checker:

    def check(t):
        return t.split(':')[0] == 'High School District'

    def parse(t):
        return t.split(':')[1].strip()

class mls_source_id_checker:

    def check(t):
        return t.split(':')[0] == 'MLS/Source ID'

    def parse(t):
        return t.split(':')[1].strip()

class lot_area_checker:

    def check(t):
        return t.split(':')[0] == 'Lot Area'

    def parse(t):
        string_num =  t.split(':')[1].strip().split(' ')[0]
        return float(string_num)

class lot_area_unit_checker:

    def check(t):
        return t.split(':')[0] == 'Lot Area'

    def parse(t):
        return t.split(':')[1].strip().split(' ')[1]

class jr_mid_school_checker:

    def check(t):
        return t.split(':')[0] == 'Jr High / Middle School'

    def parse(t):
        return t.split(':')[1].strip()

class jr_mid_school_district_checker:

    def check(t):
        return t.split(':')[0] == 'Jr High / Middle School District'
    
    def parse(t):
        return t.split(':')[1].strip()

class tax_amount_checker:

    def check(t):
        return t.split(':')[0] == 'Annual Tax Amount'

    def parse(t):
        string_num = t.split('$')[1].split(',')
        return int(string_num)
