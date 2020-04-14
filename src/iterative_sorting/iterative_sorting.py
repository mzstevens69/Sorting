# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # use first number in list and 
        #loop over right side starting with the next index      
        for next_smallest in range(cur_index+1, len(arr)):
        # is next smallest less than right side of arr--smallest index
            if arr[next_smallest] < arr[smallest_index]:
        # make new index equal to smallest index
                smallest_index =  next_smallest           
        # TO-DO: swap a,b = b,a
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr #make sure you are returning in the proper place


# TO-DO:  implement the Bubble Sort function below O(n^2)

def bubble_sort( arr ):
    for pair in range(len(arr)): #should be using a while loop?--while True:
    #loop through elements n-1    
        for i in range(len(arr) - 1): 
            pair = i
    #compare elements if arr[i] is greater move to the right    
            if arr[pair] > arr[pair + 1]:
    #swap them a,b = b,a
               arr[pair], arr[pair + 1] = arr[pair + 1], arr[pair]
               
    return arr

#INSERTION SORTING

#def insertion_sort(arr):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
#    for i in range(1, len(arr)):
#        temp = arr[i]
#        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
#        while j > 0 and temp < arr[j - 1]:
#            arr[j] = arr[j - 1]  # Slide over one element
 #           j -= 1
        # Insert at that position
#        arr[j] = temp
#    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr