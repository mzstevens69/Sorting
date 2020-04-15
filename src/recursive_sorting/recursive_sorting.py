# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    
    elements = len( arrA ) + len( arrB ) 
    merged_arr = [0] * elements #pre allocates memory by making [] of 10
    
    # TO-DO
    # i = 0 and j = 0 to rep pointers
   
    i = 0
    j = 0
    
    #loop over for elements in range
    
    for element in range(elements):
                   
    # if i pointer reaches the end of a list or goes past, add it to the other list      
        if i >= len(arrA):
            merged_arr[element] = arrB[j]
            j += 1
    # if j pointer reaches the end of a list or goes past, add it to the other list       
        elif j >= len(arrB):              
            merged_arr[element] = arrA[i]          
            i += 1
    #compare the start of arrA[i] to the start of arrB[j] 
    # the one that is smaller gets added to merged arr   
        elif arrA[i] < arrB[j]:
            merged_arr[element] = arrA[i]
            i += 1
                    
        else:
            merged_arr[element] = arrB[j]
            j += 1
    
   
    return merged_arr



#RULES FOR RECURSION
#1. Must have a base case.
#2. Must change state toward the base case.
#3. Must call itself, recursively.

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
#base case If array is empty or length of 1
    if len(arr) <= 1:
        return arr
    
# TO-DO
    # take arr and divide in half till each till len of arr's is == 1
    
    split = len(arr)//2
    # do merge sort    
    
    go_left = merge_sort(arr[:split])
    
    go_right = merge_sort(arr[split:])
    
    
    
    return merge(go_left, go_right)
    
    
    
    
    
    

    


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
