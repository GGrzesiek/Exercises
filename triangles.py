def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if((a==0)|(b==0)|(c==0)):
        return False
    elif((a==b)&(a==c)&(b==c)):
        return True
    else:
        return False

def isosceles(sides):
    if(is_triangle(sides)):
        for i in range(len(sides)):
            for j in range(i+1,len(sides)):
                if(sides[i] == sides[j]):
                    return True
    return False


def scalene(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a != b and b != c and a != c
    return False

    
def is_triangle(sides):
    a, b, c = sorted(sides) 

    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    return a + b > c

    