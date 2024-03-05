def bubbleSort(array):
  
  for i in range(len(array)):# outer loop to access each array element
    for j in range(0, len(array) - i - 1): # inner loop to compare array elements

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:# Now we swap elements if elements are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
      #end if  
    #end for
  #end for
#end def

data = [-3, 34, 1, 12, -6]

bubbleSort(data)

print('Sorted Array(Ascending Order):')
print(data)
#added