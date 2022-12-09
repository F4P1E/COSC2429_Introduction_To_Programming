def is_palindrome(s):
    """
    This function checks if a string is palindrome (read the same forward and backward)
    :param s: a string
    :return: True/False
    """
    reversed_string = s[::-1]
    if s.lower() == reversed_string.lower():  # don't forget to lower the case just in case
        return True
    else:
        return False


# main program
print(is_palindrome('hello'))
print(is_palindrome('radar'))
print(is_palindrome('Radar'))
