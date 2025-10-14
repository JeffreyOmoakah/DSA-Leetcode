# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. 

# Brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Thought process:
        # 1) The simplest (brute-force) idea is to check every pair of numbers and see if they sum to target.
        # 2) Use two nested loops: the outer loop picks the first element (index i),
        #    and the inner loop checks every following element (index j > i) to avoid repeating pairs
        #    and to avoid using the same element twice.
        # 3) As soon as we find nums[i] + nums[j] == target, return the pair of indices [i, j].
        # 4) This guarantees the first valid pair is returned; problem statement promises exactly one solution,
        #    so no need to continue searching after finding it.
        # 5) Complexity: O(n^2) time (two nested loops), O(1) extra space (only indices returned).
        #    This is fine for small inputs but will be slow for large arrays; we can later optimize using a hashmap.
        for i in range (len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]