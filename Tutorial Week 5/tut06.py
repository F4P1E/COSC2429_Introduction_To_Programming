def iter_harmonic(n):
    """
    This iterative function calculates the sum of the harmonic sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    sum_num = 0
    for i in range(1, n+1):
        sum_num += 1/i
    return sum_num


def recur_harmonic(n):
    """
    This recursive function calculates the sum of the harmonic sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 1:
        return 1
    else:
        return 1/n + recur_harmonic(n-1)


def iter_tri_num(n):
    """
    This iterative function calculates the sum of the triangular number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    sum_num = 0
    for i in range(1, n+1):
        sum_num += i
        print(sum_num)
    return sum_num


def recur_tri_num(n):
    """
    This recursive function calculates the sum of the triangular number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 1:
        return 1
    else:
        return n + recur_tri_num(n-1)


# another version if you want to print
def recur_tri_num2(n):
    """
    This recursive function calculates the sum of the triangular number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 1:
        return 1
    else:
    	i = recur_tri_num2(n-1)
    	print(i)
        return n + i


def iter_pen_num(n):
    """
    This iterative function calculates the sum of the pentagonal number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    sum_num = 1 # note the different start value and range here
    for i in range(1, n):
        sum_num += i*5
    return sum_num


def recur_pen_num(n):
    """
    This recursive function calculates the sum of the pentagonal number sequences
    :param n: a number (int)
    :return: sum of the sequences
    """
    if n == 0:
        return 1
    else:
        return n*5 + recur_pen_num(n-1)


def iter_collatz(n):
    """
    This iterative function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    max_num = 0
    while True:
        if max_num < n:
            max_num = n
        if n == 1:
            break
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
    return max_num


# Version 1: passing max_num as a parameter
max_num = 0
def recur_collatz1(n, max_num):
    """
    This recursive function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    if max_num < n:
        max_num = n
    if n == 1:
        return max_num
    else:
        print(n)
        if n % 2 == 0:
            return recur_collatz1(n/2, max_num)
        else:
            return recur_collatz1(n*3+1, max_num)


# Version 2: using max() function
def recur_collatz2(n):
    """
    This iterative function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    if n == 1:
        return 1
    else:
        print(n)
        if n % 2 == 0:
            return max(n, recur_collatz2(n/2))
        else:
            return max(n, recur_collatz2(n*3+1))


# Version 3: only 1 call of the function
def recur_collatz3(n):
    """
    This iterative function finds the max of the collatz sequences
    :param n: a number (int)
    :return: max of the sequences
    """
    if n == 1:
        return 1
    else:
        print(n)
        if n % 2 == 0:
            i = n/2
        else:
        	i = n*3+1
            return max(n, recur_collatz3(i))
