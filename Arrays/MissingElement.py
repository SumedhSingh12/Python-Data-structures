def missing_element(list1, list2):
    if len(list1) - len(list2) > 1:
        return "Missing more than 1 elements"
    else:
        element_map = {}
        for element in list2:
            if element in element_map:
                element_map[element] += 1
            else:
                element_map[element] = 1

        for element in list1:
            if element in element_map:
                element_map[element] -= 1
            else:
                return element

        for element in element_map:
            if element_map[element] > 0:
                return element