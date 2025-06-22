'''. *Minimum Swaps to Sort an Array*  
   Given an array with distinct elements, find the minimum number of swaps required to sort it'''

def minimum_swap(arr):
    swaps = 0
    i=0
    while i<len(arr):
        correct_index=arr[i]-1
        if arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            swaps +=1
        else :
            i+=1
    return swaps
print(minimum_swap([4, 3 , 2,1]))# 0

        

