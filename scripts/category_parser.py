
# def parsers = [

# ]


class bedroom_checker:
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
            num: number of bedrooms
        """
        return t.split(':')[1].strip()

