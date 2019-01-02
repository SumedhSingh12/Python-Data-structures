#Run Length compression algorithm
def compress_string(s):
    r = ""
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s + "1"
    else:
        letter_map = {}
        for letter in s:
            if letter in letter_map:
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
        for letter in letter_map:
            r+= str(letter)+str(letter_map[letter])
    return r