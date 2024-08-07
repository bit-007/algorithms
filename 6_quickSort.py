import random
import time
def quicksort(arr): 
    if len(arr) <= 1: 
        return arr 
    else: 
        pivot = arr[0] 
        left = [x for x in arr if x < pivot] 
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot] 

        return quicksort(left) + middle + quicksort(right) 

lst=[random.randint(1,100) for i in range(10) ]
print(lst)
start=time.time()
result=quicksort(lst)
end=time.time()
tim=end-start
print(result)
print(tim)