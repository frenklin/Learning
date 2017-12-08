#!/usr/bin/env python



# multiply less < 100
def countSubArrays(arr, limit):
    lp = 0
    rp = 0
    slide_val = arr[0]
    res = 0

    while lp<len(arr) and rp+1<len(arr):                

        if slide_val < limit:
            rp+=1            
            slide_val *= arr[rp] 

        if slide_val >= limit:
            print(arr[lp:rp])
            res += 1
            slide_val //= arr[lp]             
            lp += 1
            if rp+1>=len(arr) and slide_val < limit:
                print(arr[lp:rp+1])
                res+=1

        

    return res

    

a = [5, 2, 2, 10, 7, 11] # only positive  5*2*10 = 100  2*10 = 20 10*7=70 7*11 = 77 =>>> 4

print(countSubArrays(a, 100))

