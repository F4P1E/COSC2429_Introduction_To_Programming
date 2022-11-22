# import the even.pyfile as a module (the files have to be in the same folder)

import even


def is_odd(n):
    """
    This function will check if the number is odd or not
    :param n: an integer
    :return: True/False
    """
    # calling the is_even(n) function to check if n i an even number
    if even.is_even(n):
        return False
    else:
        return True

    #  Testing the function
    print(is_odd(5))
