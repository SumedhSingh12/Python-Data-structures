def frequencySort(s):
        freq = {}
        res = ""
        for letter in s:
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1
        result = list(freq.keys())
        for i in range(0,len(result)):
            max = max_finder(result, i, freq)
            result[i], result[max] = result[max], result[i]
        for _ in result:
            res += _ * freq[_]
        return res
def max_finder(result, i, freq):
    max = i
    for index in range(i, len(result)):
        if freq[result[index]] > freq[result[max]]:
            max = index
    return max
print(frequencySort("cccaaa"))