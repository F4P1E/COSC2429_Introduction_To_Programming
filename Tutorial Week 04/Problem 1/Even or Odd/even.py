def is_even(n):
    """
    This function will check the number even or odd
    :param n: an integer
    :return: True/False
    """

    # check if n is divisible by 2
    if n % 2 == 0:
        return True
    else:
        return False

    # testing function
    print(is_even(5))


