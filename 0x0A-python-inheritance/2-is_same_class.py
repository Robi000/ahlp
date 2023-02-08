#!/usr/bin/python3

"""1-my_list
Contains class MyList, subclass of standard type list
"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (obj): any object 
        a_class (class): classobj 
    """

    return obj.__class__.__name__ == a_class.__name__