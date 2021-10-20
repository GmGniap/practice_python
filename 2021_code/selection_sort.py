find_range = [2,10,9,8,1,0,19]
def find_smallest(arr):
    smallest_value = arr[0]
    smallest_index = 0 
    for i in range(1,len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return(smallest_index)

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort(find_range))