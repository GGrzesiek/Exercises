def is_isogram(word_or_phrase):
    clean_string = word_or_phrase.lower()

    clean_string = clean_string.replace(' ', '').replace('-', '')

    letter_set = set()
    for char in clean_string:
        if char in letter_set:
            return False
        letter_set.add(char)
    
    return True
