#!/usr/bin/python3
'''Module 6-peak
Contains function find_peak
'''


def find_peak(list_of_integers):
    '''
    find the pic and return it ! check the emptyness
    '''
    if len(list_of_integers) == 0:
        return None
    return sorted(list_of_integers)[-1]
