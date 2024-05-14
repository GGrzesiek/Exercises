def steps(number):
    steps_number = 0
    if number > 0:
        while(number!=1):
            if(number%2==0):
                number /= 2
                steps_number+=1
            elif((number+1)%2==0):
                number = ((3*number)+1)
                steps_number+=1
    else: raise ValueError("Only positive integers are allowed")
    return steps_number