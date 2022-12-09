def multiplybtimes(a, b):
    """

    :param a: a number
    :param b: times a need to be multiplied
    :return:
    """
    if b == 1:
        return a
    return a + multiplybtimes(a, b-1)
