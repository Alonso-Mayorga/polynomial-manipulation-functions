# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:28:58 2021

@author: galgo
"""

def polynomial_product(p1, p2):
    """
    Calculates the product of two polynomials represented as lists of coefficients.

    :param p1: List of coefficients of the first polynomial.
    :type p1: list[float or int]
    :param p2: List of coefficients of the second polynomial.
    :type p2: list[float or int]
    :return: List of coefficients of the polynomial resulting from the product.
    :rtype: list[float or int]
    :raises TypeError: If the parameters are not lists or the elements are not real numbers.
    """
    if not isinstance(p1, list) or not isinstance(p2, list):
        raise TypeError('Parameters must be lists')
    for i in range(len(p1)):
        if not isinstance(p1[i], int) and not isinstance(p1[i], float):
            raise TypeError('Elements of the lists must be real numbers')
    for i in range(len(p2)):
        if not isinstance(p2[i], int) and not isinstance(p2[i], float):
            raise TypeError('Elements of the lists must be real numbers')
    while len(p1) < len(p2):
        p1.insert(0, 0)
    while len(p2) < len(p1):
        p2.insert(0, 0)
    p = [0]*((2*len(p2))-1)
    for i in list(range(0, len(p))):
        print('i ' +str(i))
        for j in list(range(0, i+1)):
            if j < len(p1) and (i-j) < len(p2):
                print('j ' + str(j))
                p[i]=p[i]+(p1[j]*p2[i-j])
    while p[0] == 0:
        del p[0]
    print('The coefficients of the polynomial product are given by the list ' + str(p))
    return(p)
