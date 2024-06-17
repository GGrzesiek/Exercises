def square_root(number):
    """Calculate the square root of a number without build-in functions.

    :param number: int - number to calculate the square root of.
    :return: float - square root of the provided number.
    """
    e = 2.718281828459045 # approximate of e
    def ln(x): # using one of ln identities
        n = 1000000.0 # increasing n gives better precision
        return n * ((x ** (1/n)) - 1)
    powr = 0.5*(ln(number))
    return int(e**(powr)) # added int casting because exercise wanted int answer, for further use it can be deleted
    
    

