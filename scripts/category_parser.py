
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
    