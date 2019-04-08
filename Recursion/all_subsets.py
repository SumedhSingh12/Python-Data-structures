def all_subsets(arr):
    subset = [None] * len(arr)
    all_subsets_helper(arr, subset, 0)

def all_subsets_helper(arr, subset, i):
    if i == len(arr):
        print(subset)
    else:
        subset[i] = None
        all_subsets_helper(arr, subset, i+1)
        subset[i] = arr[i]
        all_subsets_helper(arr, subset, i+1)

all_subsets([1,2,3,4])