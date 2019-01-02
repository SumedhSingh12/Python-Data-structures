def efficient_anagram(string1, string2):
    
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    string1 = string1.lower()
    string2 = string2.lower()
    
    if len(string1) != len(string2):
        return False
    
    letter_map = {}
    
    for letter in string1:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    for letter in string2:
        if letter in letter_map:
            letter_map[letter] -= 1
        else:
            return False

    for i in letter_map.values():
        if i > 0:
            return False
    
    return True 