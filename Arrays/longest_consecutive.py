def longest_consecutive(s):
    result = {}
    curr_longest = 0
    longest = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            curr_longest += 1
        else:
            longest = max(longest, curr_longest+1)
            result[curr_longest+1] = s[i-1]
            curr_longest = 0
    return str(result[longest])+" : "+str(longest)
print(longest_consecutive("AABCDDBBBEA"))