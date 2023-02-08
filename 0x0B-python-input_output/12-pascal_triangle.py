#!/usr/bin/python3

"""11-student
pasical tryangle 
"""


def pascal_triangle(n):
    """pasical tryangle 

    Args:
        n (int ): no of row

    Returns:
        list of list : pasical tryangel 
    """
    if n <= 0:
        return []
    a = []
    for i in range(n):
        new = [0] * (i+1)
        new[0], new[-1] = 1, 1
        if i > 1:
            for j in range(1, i):
                new[j] = a[-1][j-1] + a[-1][j]
        a.append(new)

    return (a)
