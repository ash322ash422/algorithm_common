
def partition(array, low, high): # function to find the partition position

  pivot = array[high] # choose the rightmost element as pivot
  i = low - 1 # pointer for greater element

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
    #end if
  #end for
  
  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1 # return the position from where partition is done
#end def

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    quickSort(array, low, pi - 1) # recursive call on the left of pivot
    quickSort(array, pi + 1, high)# recursive call on the right of pivot
#end def

data = [9, 8, 3, 2, 0, 10, 7]
size = len(data)
quickSort(data, 0, size - 1)

print('Sorted Array (Ascending Order):')
print(data)