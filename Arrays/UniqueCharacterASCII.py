import numpy as np

def unique_char(s):
    if len(s) > 128:
        return False
    char_array = np.zeros((128), dtype = bool) #Creating a numpy array with 128 false
    for char in s:
        val = ord(char)
        if char_array[val]:
            return False
        char_array[val] = True
    return True