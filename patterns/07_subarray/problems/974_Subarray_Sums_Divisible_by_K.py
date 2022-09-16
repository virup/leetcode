# 974. Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
#
# Here we have to find the subarrays whose sum is divisible by K.
# We keep a running prefixSum and a dictionary of prefixSums.
# For every prefixSum we find the remainder when divided by K.
# and store it in the dictionary. We also find if there is a
# prefixSum who has a remainder of K earlier. If yes, thats
# a candidate for subarray

from collections import defaultdict
from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        noOfSubarrays = 0
        remainderKMap = defaultdict(lambda: 0)
        remainderKMap[0] = 1

        for n in nums:
            prefixSum += n
            remainder = prefixSum % k
            if remainder < 0:
                remainder = remainder + k
            noOfSubarrays += remainderKMap[remainder]
            remainderKMap[remainder] += 1

        return noOfSubarrays
