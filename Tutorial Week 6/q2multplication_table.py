import numpy as np
import pandas as pd

n = 12

def mult_table(n):
    """
    This function generates multiplication table in numpy matrix format
    :param n: the max number of multiplication
    :return: matrix of multiplication table
    """
    rng = np.arange(0, n+1)
    return rng * rng[:, None]


# print with numpy without header
print(mult_table(n))

# print with pandas without header
print(pd.DataFrame(mult_table(n)).to_string(header=False))

'''
native python way 
this is not a very good way 
since you have to manually update the number in the format function
'''
print('{:>5s}'.format('x'), end='')
for val in range(0, n):
    print('{:5d}'.format(val), end='')
print('')
for val in range(0, n):
    print('{:5d}'.format(val), end='')
    for in_val in range(0, n):
        end_val = in_val*val
        print('{:5d}'.format(end_val), end='')
    print('')