def is_valid(isbn):
    clean_string = isbn.replace('-', '')
    sum = 0
    dec = 0  # decrementor
    if len(clean_string) != 10 or not (clean_string[-1].isdigit() or clean_string[-1] == 'X'): # check if the string is 10 characters long and the last character is a digit or 'X'
        return False
    
    for char in clean_string[:-1]:
        if char.isalpha():
            return False
        
    if clean_string[-1] == 'X':
        for char in clean_string[:-1]:
            sum += int(char) * (10 - dec)
            dec += 1
        sum += 10 # adding 'X' that equals 10
    elif clean_string[-1].isdigit():
        for char in clean_string:
            sum += int(char) * (10 - dec)
            dec += 1

    return bool(sum % 11 == 0)