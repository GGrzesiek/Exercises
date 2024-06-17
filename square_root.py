def square_root(number):
    """Calculate the square root of a number without build-in functions.

    :param number: int - number to calculate the square root of.
    :return: float - square root of the provided number.
    """
    last_digit = {0:0,1:[1,9],4:[2,8],9:[3,7],6:[4,6],5:5} # last number from pow

    number_str = str(number)
    last = int(number_str[-1])
    rest = int(number_str[:-2])
    print(f"dupa {last} ddad {rest}")
    first_root = 1
    while first_root^2 <= int(rest): # calculating number whose power is closest to rest while not exceeding it
        first_root += 1

    if (last!=0 & last !=5): # if we have more than 1 option
        choices = last_digit[last]
        if(first_root * (first_root + 1) < rest):
            result =str(first_root) + str(choices[1])
            print(result)
    else:
        pass
    
    

