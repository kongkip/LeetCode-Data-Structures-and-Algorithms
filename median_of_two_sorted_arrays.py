from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    i = 0
    j = 0

    # swap the arrays such that length of nums1 <  length of nums2
    if n < m:
        temp = n
        n = m
        m = temp
        temp = nums1
        nums1 = nums2
        nums2 = temp

    min_index = 0
    max_index = m
    median = 0

    while min_index <= max_index:
        i = (min_index + max_index) // 2
        j = ((n + m + 1) // 2) - i

        """ 
        checking for the following conditions
            - if i = m  the elements from nums1 in the second half is empty.
            - if j = 0 the elements from nums2 in the first half is empty.

            - if i = 0  the elements from nums1 in the first half is empty.
            - if j = n the elements from nums2 in the second half is empty.
        """

        # searching on the right
        if i < m and j > 0 and nums2[j - 1] > nums1[i]:
            min_index = i + 1

        # searching on the left
        elif i > 0 and j < n and nums2[j] < nums1[i - 1]:
            max_index = i - 1
        else:
            if i == 0:  # if there are no elements in first half of nums1
                median = nums2[j - 1]
            elif j == 0:  # if there are no elements in first half of nums2
                median = nums1[i - 1]
            else:
                median = max(nums1[i - 1], nums2[j - 1])
            break

    if (m + n) % 2 == 1:  # if the number of elements is odd there is one middle element
        return median
    if i == m:
        return (median + nums2[j]) / 2.0
    if j == n:
        return (median + nums1[i]) / 2.0

    return (median + min(nums1[i], nums2[j])) / 2.0


if __name__ == '__main__':
    _nums1 = [1, 2]
    _nums2 = [3, 4, 5, 6]
    _median = findMedianSortedArrays(_nums1, _nums2)
    print(f"Median of {_nums1} and {_nums2} is {_median:4f}")
