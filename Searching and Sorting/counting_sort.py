def counting_sort(unsorted_list, max_element):
    
    # list of 0s at indices 0 to max_price
    count_list = [0] * (max_element+1)
    
    #Populating the elements with their number of occurences in the count_list
    for ele in unsorted_list:
        count_list[ele] += 1
    
    #Creating a new list to store the elements in a sorted way.
    sorted_list = []
    
    for element, count in enumerate(count_list):
        for time in range(count):
            sorted_list.append(element)
    return sorted_list
    
counting_sort([4,6,2,7,3,8,9],9)