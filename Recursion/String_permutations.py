def permute(s):
    output = []
    if len(s) <= 1:
        output = [s]
    else:
        for index,letter in enumerate(s):
            for perm in permute(s[:index] + s[index+1:]):
                output += [letter+perm]
    return output
permute('abc')