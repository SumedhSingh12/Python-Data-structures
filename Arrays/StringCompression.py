def compress_str(s):
    count = 1
    res = s[0]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            res += str(count)
            res += s[i+1]
            count = 1
    res += str(count)
    return res
compress_str("AAABBCCA")
