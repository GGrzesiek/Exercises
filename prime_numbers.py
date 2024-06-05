def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    root = int(n**0.5) + 1
    for div in range(3, root, 2):
        if n % div == 0:
            return False
    return True