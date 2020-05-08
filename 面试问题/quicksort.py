
import random

def quicksort(arr=[]):
    if len(arr) <= 2:
        return arr
    
    pirot = random.sample(arr,1)[0]
    print(pirot)
    low_list = [ x for x in arr if x < pirot]
    print(low_list)
    high_list = [ x for x in arr if x > pirot]
    print(high_list)
    eq_list = [ x for x in arr if x == pirot]


    return quicksort(low_list) + eq_list + quicksort(high_list)


a = [6,1,1,5,2,6,3,9,4]
print(quicksort(a))