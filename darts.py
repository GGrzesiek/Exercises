import math
def score(x, y):
    """
    Return score based on distance from center of dartboard.

    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.

    The outer circle has a radius of 10 units (this is equivalent to the total radius for the entire target),
    the middle circle a radius of 5 units, and the inner circle a radius of 1. 
    """
    distance = math.sqrt(x**2 + y**2)
    if(distance<= 1):
        return 10
    elif(distance <= 5):
        return 5
    elif(distance <= 10):
        return 1
    else: return 0