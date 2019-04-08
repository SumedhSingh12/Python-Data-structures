def first_recurring(s):
    seen = set()
    for letter in s:
        if letter in seen:
            return letter
        else:
            seen.add(letter)

def first_nonrecurring(s):
    seen = {}
    for letter in s:
        if letter in seen:
            seen[letter] += 1
        else:
            seen[letter] = 1
    for letter in seen:
        if seen[letter] == 1:
            return letter
            
print("First Recurring character: " + str(first_recurring("aabccbdcbe")))
print("First Non-Recurring character: " + str(first_nonrecurring("aabccbdcbe")))