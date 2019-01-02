def unique_char(s):
    char_pool = set()
    for letter in s:
        if letter in char_pool:
            return False
        else:
            char_pool.add(letter)
    return True