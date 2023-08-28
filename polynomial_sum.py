# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:41:22 2021

@author: galgo
"""

def polynomial_sum(p1, p2):
    """
    Calculates the sum of two polynomials represented as lists of coefficients.

    :param p1: List of coefficients of the first polynomial.
    :type p1: list[float or int]
    :param p2: List of coefficients of the second polynomial.
    :type p2: list[float or int]
    :return: List of coefficients of the polynomial resulting from the sum.
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
    suma = [0] * len(p1)
    for i in range(len(p1)):
        suma[i] = p1[i] + p2[i]
    while suma[0] == 0:
        del suma[0]
    print('The coefficients of the polynomial sum are given by the list ' + str(suma))
    return(suma)
