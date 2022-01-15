# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        # Create the array
        arr = []
        for i in range(n):
            arr.append(i + 1)

        # Run the permutation (k-1) times
        for i in range(k - 1):
            permute(arr)

        # Create a string of the results
        res = ""
        for i in range(len(arr)):
            res += str(arr[i])
        return res


def permute(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    # 1. Find the first decreasing element from the right
    DEIndex = -1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > nums[i - 1]:
            DEIndex = i
            break

    # If there is no such element, then the array is at the last
    # sequence (for ex. [3,2,1]). So simply reverse and return
    if DEIndex == -1:
        nums.reverse()
        return

    # 2. Find the just larger element compared to DE
    JLIndex = len(nums) - 1
    while nums[JLIndex] <= nums[DEIndex]:
        JLIndex -= 1

    if JLIndex == DEIndex:
        # No such element
        JLIndex = len(nums) - 1

    # 3. Swap
    temp = nums[DEIndex]
    nums[DEIndex] = nums[JLIndex]
    nums[DEIndex] = temp

    # 4. Reverse all the elements to the right of DEIndex
    nums[DEIndex + 1:] = nums[DEIndex + 1:][::-1]