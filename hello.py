def Bubble_sort(array):
    array = array[:]
    n = len(array)
    for i in  range (n):
        swapped = False
        for j in range (0,n-i-1):
            if array [j] > array [j+1]:
                swapped = True
                array [j],array [j+1] = array[j+1] , array[j]
                if not swapped:
                    break
              
    return array

print(Bubble_sort([25,25,0,6,25,24,29,84,10]))
