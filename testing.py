
def reverseArray(a):
    # Write your code here
    size = len(a)
    #if only one element present, then return the array
    if(size==1):
        return arr
     
    #if only two elements present, then swap both the numbers.
    elif(size==2):
        arr[0],arr[1],=arr[1],arr[0]
        return arr
     
    #if more than two elements presents, then swap first and last numbers.
    else:
        i=0
        while(i<size//2):
 
            #swap present and preceding numbers at time and jump to second element after swap
            arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
       
            #skip if present and preceding numbers indexes are same
            if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
                arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
            i+=2
        #end while
        return arr    
if __name__ == '__main__':
    input = "1 4 3 2 7 "
    arr = list(map(int, input.rstrip().split()))
    print("arr=",arr)
    
    res = reverseArray(arr)
    print("rev=", res)
    