def selectionSort(array):
    
    for i in range (0, len(array)-1):
        j=i
        min=array[j]
        minpos=-1
        while(j<len(array)):
            if array[j] <min:
                min=array[j]
                minpos=j
            j+=1
        if(minpos>0 and array[minpos]<array[i] ):
            swap(i, minpos, array)

def swap(i, j, array):
    array[i], array[j]= array[j], array[i]


arr1=[1,2]
print(arr1)
selectionSort(arr1)
print("Sorted array:", arr1)


