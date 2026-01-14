"Binary Search"
# goal to find the index of an item in an array


def binary(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1
            
        else:
            begin_index = midpoint + 1
            
    return None

    
    
print(binary([1, 2, 3, 4, 5, 6], 5))
            