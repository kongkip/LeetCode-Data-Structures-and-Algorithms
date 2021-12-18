from typing import List
import unittest


def find_length(nums1: List[int], nums2: List[int]) -> int:
    max_len = 0
    m = len(nums1)
    n = len(nums2)

    # dp[][] array
    dp = [[0 for i in range(m + 1)] for i in range(n + 1)]

    # Updating the dp[][] table in Bottom up approach
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # If nums1[i] is equal to nums2[i] then dp[j][i] = dp[j+1][i+1] + 1
            if nums1[i] == nums2[j]:
                dp[j][i] = dp[j + 1][i + 1] + 1


    # Find maximum of all the values in dp[][] array to get the maximum length
    for i in dp:
        for j in i:
            max_len = max(max_len, j)
    return max_len


class TestFindLength(unittest.TestCase):

    def test_find_length(self):
        _nums1 = [1, 2, 3, 2, 1]
        _nums2 = [3, 2, 1, 4, 7]
        self.assertEqual(find_length(_nums1, _nums2), 3, "Should be 3")

TestFindLength().test_find_length()
