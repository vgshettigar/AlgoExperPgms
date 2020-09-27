def insertionSort(array):
    for i in range(1, len(array)):
        j=i
        while j>0 and array[j]< array[j-1]:
            swap(j, j-1, array)
            j-=1

def swap(i, j, array):
    array[i], array[j]= array[j], array[i]

arr1=[8, 5, 2, 9, 5, 6, 3]
print(arr1)
insertionSort(arr1)
print("Sorted array:", arr1)