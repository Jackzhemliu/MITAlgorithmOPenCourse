import numpy as np  


def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -np.inf
    sum_cross = 0
    max_left = mid 
    for i in np.linspace(mid, low, mid-low+1).astype(int):
        sum_cross = sum_cross + arr[i]
        if sum_cross > left_sum:
            left_sum = sum_cross 
            max_left = i 
    
    right_sum = -np.inf
    sum_cross = 0 
    max_right = mid 
    for j in np.linspace(mid+1,high, high-mid).astype(int):
        sum_cross = sum_cross + arr[j]
        if sum_cross> right_sum :
            right_sum = sum_cross 
            max_right = j 
    
    return max_left, max_right, left_sum+right_sum 
    


def find_maximum_subarray(arr, low, high): 
    if (high==low):
        return (low, high, arr[low])
    else:
        mid = ((low+high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
        right_low, right_high, right_sum=find_maximum_subarray(arr, mid+1, high)
        cross_low, cross_high, cross_sum= \
         find_max_crossing_subarray(arr, low, mid, high)
        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >=left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum 
        else:
            return cross_low, cross_high, cross_sum 
