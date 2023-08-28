def monic_factors(p):
    """
    Computes the monic irreducible factors of a polynomial represented as a list of coefficients.

    :param p: List of coefficients of the polynomial.
    :type p: list[int]
    :return: Tuple containing a list of lists representing monic irreducible factors and a list of coefficients
             representing the remaining irreducible polynomial.
    :rtype: tuple[list[list[int]], list[int]]
    :raises TypeError: If the parameter is not a list or its elements are not integers.
                      If the first element of the list is not 1.
    """
    if not isinstance(p, list):
        raise TypeError('Parameter must be a list')
    for i in range(len(p)):
        if not isinstance(p[i], int):
            raise TypeError('Parameter must be a list with integer elements')
    if p[0] != 1:
        raise TypeError('Parameter must be a list with first element 1')
    factores = []
    factoresti = []
    while p[-1] == 0:
        del p[-1]
        factores.append([1, 0])
    pp = p.copy()
    p2 = [pp, p]
    if abs(p[-1]) != 1:
        factoresti = [1, -1, p[-1], -p[-1]]
        for i in range(2, abs(p[-1])):
            if p[-1] % i == 0:
                factoresti.append(i)
                factoresti.append(-i)
    else:
        factoresti = [1, -1]
    t = True
    while t == True:
        t = False
        for i in range(0, len(factoresti)):
            for j in range(0, len(p2[0])-1):
                p2[0][j+1] = p2[0][j+1] + (p2[0][j]*factoresti[i])
            if p2[0][-1] == 0:
                t = True
                factores.append([1, -factoresti[i]])
                del p2[0][-1]
                nueva = p2[0].copy()
                p2.insert(0, nueva)
            else:
                p2[0] = p2[1].copy()
        if len(p2[0]) == 1:
            print('The coefficients of the monic irreducible factors are ' + str(factores) + ' and there are no complex roots.')
            return(factores, [1])
    print('The coefficients of the monic irreducible factors are ' + str(factores) + ' and the coefficients of the remaining irreducible polynomial are ' + str(p2[0]) + '.')
    return(factores, p2[0])




