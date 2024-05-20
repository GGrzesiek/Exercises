def is_armstrong_number(number):
    """Checks if a number is an armstrong number and returns a boolean value."""
    sum = 0
    digitlist = [int(digit) for digit in str(number)]
    dignum = len(digitlist)
    if(number > 9):
        for i in digitlist:
            sum += pow(i,dignum)
    else:
        return True
    if(sum == number):
        return True
    else:
        return False
        
        
