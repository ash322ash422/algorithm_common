def insertionSort(array):
    
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]: # For descending order, change key<array[j] to key>array[j]
            array[j + 1] = array[j]
            j = j - 1
        #end while
        
        array[j + 1] = key # Place the key at after the element just smaller than it.
    #end for
#end def

data = [10, 4, 0, 3, 5]
insertionSort(data)
print('Sorted Array (Ascending Order):')
print(data)