def msg_decode(data):
    mem = [None] * (len(data)+1)
    return decode(data, len(data), mem)
def decode(data, k, mem):
    if k == 0:
        return 1
    elif mem[k]:
        return mem[k]
    index = len(data) - k
    if data[index] == "0":
        return 0
    result = decode(data, k-1, mem)
    if k >= 2 and int(data[index:index+2]) <= 26:
        result += decode(data, k-2, mem)
    mem[k] = result
    return mem[k]
msg_decode("1234561")