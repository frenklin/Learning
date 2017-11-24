#!/usr/bin/env python

INT_MAX = 2147483647
#INT_MIN = (-INT_MAX - 1)

def divide(dividend, divisor):

    sign = 1 if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0) else -1
    
    dvd = abs(dividend)
    dvs = abs(divisor)
    
    if dvs == 1:
        if dvd > INT_MAX and sign > 0:
            return INT_MAX
        return dvd * sign

    d = dvs
    bit_num = 32*[0]
    bit_num[0] = d
    i=0
    while d <= dvd:
        i+=1
        bit_num[i] = d = d << 1    
    i-=1

    result = 0
    while(dvd >= dvs):
        if dvd >= bit_num[i]:
            dvd -= bit_num[i]
            result += (1<<i)
        else:
            i-=1     
    
    if result > INT_MAX and sign > 0:
        return INT_MAX
    
    return result * sign



print(divide(-2147483648, -1))
print(divide(15240729615,1234567))

