# solving by reversal
# let AB be two parts of the input array A=arr[0..d-1] and B=arr(d..n-1).

"""
procedure
- Reverse A to get ArB, where Ar is reverse of A.
- Reverse B to get ArBr, where Br is reverse of B.
- Reverse all to get (ArBr)r=BA


    Example 
    - let the array be arr[] = [1, 2, 3, 4, 5, 6, 7], d=2, and n=7
    A=[1, 2] and B=[3,4,5,6,7]

    Reverse A, we get ArB = [2, 1, 3, 4, 5, 6, 7]
    Reverse B, we get ArBr = [2, 1, 7, 6, 5, 4, 3]
    Reverse all, we get (ArBr)r = [3, 4, 5, 6, 7, 1, 2]
"""


def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def left_rotate(arr, d):
    # if the d < 0 return nothing
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is greater than array length
    d = d % n
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)

    return arr


if __name__ == "__main__":
    _arr = [1, 2, 3, 4, 5, 6, 7]
    _d = 2
    rotated_arr = left_rotate(_arr, _d)
    for i in range(len(rotated_arr)):
        print(f"{rotated_arr[i]}", end=" ")
