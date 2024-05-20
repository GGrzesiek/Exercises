def leap_year(year):
    """Check if a year is a leap year"""
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else: return False
        else: return False
    else: return False