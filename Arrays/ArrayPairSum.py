def array_pair(array, target_sum):

    if len(array) <2:
        return

    seen = set()
    output = set()

    for number in array:
        if (target_sum - number ) in seen:
            output.add((min(number, target_sum - number), max(number, target_sum - number)))
        else:
            seen.add(number)

    print(str(len(output))+" pairs found")
    return output