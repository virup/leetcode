# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
#
# Finding out the number of subarrays whose sum equals K.
# Maintain a running prefix sum of all the elements of the array.
# We also store the prefixSums in a hashmap to access them quickly.
# Then find the difference of prefixSum from k. Then we check if
# previously there were any prefixSum which is equal to the difference.
# diff = sum(nums[0...i]) - k
# If there is a prefixSum (sum(nums[0..j]) then nums[j..i] is the
# required contagious subarray which sums to K.
#
# runtime complexity: 0(n) [iterate over all the elements in the array]
# memory complexity: O(n) [storing the previous prefixsums]

from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        noOfRequiredSubarrays = 0
        prefixSum = 0
        prefixSumsMap = defaultdict(lambda: 0)
        prefixSumsMap[0] = 1

        for n in nums:
            prefixSum += n
            requiredVal = prefixSum - k
            noOfRequiredSubarrays += prefixSumsMap[requiredVal]
            prefixSumsMap[prefixSum] = prefixSumsMap[prefixSum] + 1

        return noOfRequiredSubarrays