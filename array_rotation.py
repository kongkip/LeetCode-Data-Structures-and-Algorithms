# left rotate an array by d
from timeit import timeit


def left_rotate(arr, d):
    for i in range(d):
        arr = left_rotate_by_one(arr)
    return arr


# Left rotate and array of size n by one
def left_rotate_by_one(arr):
    n = len(arr)
    # store the array[0] in a temporary var
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]  # move arrays to the left
    arr[n - 1] = temp
    return arr


if __name__ == "__main__":
    _arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    rotated_arr = left_rotate(_arr, 1)
    for i in range(len(rotated_arr)):
        print(f"{rotated_arr[i]}", end=" ")
