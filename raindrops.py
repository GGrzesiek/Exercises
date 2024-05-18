def convert(number):
    if(number % 3 == 0):
        if(number % 5 == 0):
            if(number % 7 == 0):
                return "PlingPlangPlong"
            return "PlingPlang"
        elif(number % 7 == 0):
            return "PlingPlong"
        else:
            return "Pling"
    if(number % 5 == 0):
        if(number % 7 == 0):
            return "PlangPlong"
        else:
            return "Plang"
    if(number % 7 == 0):
        return "Plong"
    else:
        number = str(number)
        return number
        
            
