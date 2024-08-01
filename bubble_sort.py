def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  
        for j in range(n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]    
                print(arr)
    return arr
my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(my_list)
#compare first two elements, if first is greater swap them
#move to the next set of elements and repeat until you reach the end of the list
#then repeat these two steps until you cannot do a swap anymore