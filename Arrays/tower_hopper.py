def is_hoppable(arr):
    current_tower = 0
    while True:
        if current_tower >= len(arr):
            return True
        elif arr[current_tower] == 0:
            return False
        current_tower += arr[current_tower]
is_hoppable([4,2,0,2,0,0])
is_hoppable([1,0])