"""
Hunter McMahon
CIS 210
Project 9
Description: all your info belong to us
"""
# You can test.py your doctests with python -m doctest p9_1.py -v
import re


# done
def validate_social_security_number(social_security: str) -> bool:
    """Validate social security number, e.g., 123-45-6789 (no spaces)
    Args:
        social_security: social security number to validate
    Returns:
        True if social security is valid, False otherwise
    >>> validate_social_security_number('123-45-6789')
    True
    >>> validate_social_security_number('123456789')
    False
    >>> validate_social_security_number('123 45 6789')
    False
    >>> validate_social_security_number('123 6789')
    False
    """
    valid = re.match('^\d{3}[-]\d{2}[-]\d{4}$', social_security)
    if valid:
        return True
    else:
        return False


# done
def validate_zip(zip: str) -> bool:
    """Validate zip code (5 digits), e.g, '12345' is valid, '1 23 45' is not.
    Args:
        zip: zip code to validate
    Returns:
        True if zip is valid, False otherwise
    >>> validate_zip('12345')
    True
    >>> validate_zip('1 23 45')
    False
    >>> validate_zip('1245')
    False
    >>> validate_zip('never gonna give you up, never gonna let you down')
    False
    >>> validate_zip('12345-4321')
    False
    """
    valid = re.match('^\d{5}$', zip)
    if valid:
        return True
    else:
        return False


# done
def validate_zip_plus(zip_plus: str) -> bool:
    """Validate zip plus code, five digits followed by a dash and four more digits, 
        e.g., 41243-1234 (no spaces).
    Args:
        zip_plus: zip plus code to validate
    Returns:
        True if zip plus is valid, False otherwise
    >>> validate_zip_plus('41243-1234')
    True
    >>> validate_zip_plus('41243 1234')
    False
    >>> validate_zip_plus('412431234')
    False
    >>> validate_zip_plus('412-1234')
    False
    >>> validate_zip_plus('bruh')
    False
    """
    valid = re.match('^\d{5}-\d{4}$', zip_plus)
    if valid:
        return True
    else:
        return False


def validate_phone(phone: str) -> bool:
    """Validate phone number, e.g., 123-456-7890 or (123)456-7890 or 123.456.7890
    Args:
        phone: phone number to validate
    Returns:
        True if phone is valid, False otherwise

    >>> validate_phone('(123) 456-7890')
    True
    >>> validate_phone('(123)456-7890')
    True
    >>> validate_phone('123-456-7890')
    True
    >>> validate_phone('123.456.7890')
    True
    >>> validate_phone('(123)4567890')
    False
    >>> validate_phone('456-7890')
    False
    >>> validate_phone('123 456-7890')
    False
    """
    valid = re.match('^\(*\d{3}((\)\s*)|([.-]))?\d{3}[\s.-]\d{4}$', phone)
    if valid:
        return True
    else:
        return False


def validate_email(email: str) -> bool:
    """Validate email address, e.g., myname212@thing1.thing2.com (case-insensitive).
    Args:
        email: email address to validate
    Returns:
        True if email is valid, False otherwise
    >>> validate_email('bnorris2@uoregon.edu')
    True
    >>> validate_email('norris@cs.uoregon.edu')
    True
    >>> validate_email('yippee_skippy@yee-haw.wheeeee')
    True
    >>> validate_email('fun-times@Deschutes.hall.uoregon.edu')
    True
    >>> validate_email('b@norris2@uoregon.edu')
    False
    >>> validate_email('b norris@uoregon.edu')
    False
    >>> validate_email('bnorris2@uoregon..edu')
    False
    >>> validate_email('norris@uoregon.edu-org')
    False
    """
    # TODO: Add regex + doctest
    valid = re.match('^([\w\._-]+@+[\w_-]+(?:\.\w+)+)$', email)
    if valid:
        return True
    else:
        return False


def main():
    """Use this main to do your own function calls and other testing, it will not be used in 
    grading."""


# --- You shouldn't need to change final_main ----
def final_main():
    """Run all the functions in this file."""
    for what in ['social_security_number', 'zip', 'zip_plus', 'email', 'phone']:
        func = globals()['validate_' + what]  # the function to call
        user_input = input(f"Please enter {what}: ")
        if func(user_input):  # call the function
            print(f"{user_input} is a valid {' '.join(what.split('_'))}.")
        else:
            print(f"{user_input} is NOT a valid {' '.join(what.split('_'))}.")


if __name__ == '__main__':
    main()
    # final_main()  # uncomment if you want to call all functions in this file
