#!/usr/bin/env python

""""""


def med(arr1, arr2):
    m, n = len(arr1), len(arr2)
    if m > n:
        arr1, arr2, m, n = arr2, arr1, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = int((imin + imax) / 2)
        j = int(half_len - i)
        if i < m and arr2[j-1] > arr1[i]: 
            imin = i + 1
        elif i > 0 and arr1[i-1] > arr2[j]:
            imax = i - 1
        else:
            if i == 0: max_of_left = arr2[j-1]
            elif j == 0: max_of_left = arr1[i-1]
            else: max_of_left = max(arr1[i-1], arr2[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = arr2[j]
            elif j == n: min_of_right = arr1[i]
            else: min_of_right = min(arr1[i], arr2[j])

            return (max_of_left + min_of_right) / 2.0


ar1 = [1,2]
ar2 = [3,4]

print(med(ar1, ar2))
