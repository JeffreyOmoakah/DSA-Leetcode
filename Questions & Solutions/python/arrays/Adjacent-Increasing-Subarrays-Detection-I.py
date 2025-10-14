# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a and b (a < b), where:
#
# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Thought process:
        # 1) The goal is to find two back-to-back subarrays (each of length k) that are both strictly increasing.
        # 2) The two subarrays are adjacent, meaning the second starts right after the first ends.
        #    So if the first starts at index a, the second starts at index a + k.
        # 3) We'll loop through all valid starting indices for the first subarray.
        #    The last possible start is (len(nums) - 2*k), since we need room for both subarrays.
        # 4) For each starting index i:
        #       - Check if the subarray nums[i : i + k] is strictly increasing.
        #       - Check if the next subarray nums[i + k : i + 2k] is also strictly increasing.
        # 5) If both checks return True for any i, return True immediately.
        # 6) If no such pair is found after checking all positions, return False.
        # 7) Time complexity: O(n * k) since we may check up to n indices and each check takes O(k).
        #    Space complexity: O(1), only using variables and helper function.
        
        # loop through possible starting points for the first subarray
        for i in range(0, len(nums) - 2 * k + 1):

            # check the first subarray
            first_increasing = self.check_if_increasing(nums, i, k)

            # check the second (adjacent) subarray
            second_increasing = self.check_if_increasing(nums, i + k, k)

            # if both are strictly increasing → we found it
            if first_increasing and second_increasing:
                return True

        return False

    # helper function to check if a subarray of length k is strictly increasing
    def check_if_increasing(self, nums, start, k):
        # Thought process:
        # 1) Iterate through the subarray from start to start + k - 1.
        # 2) At each step, compare the current element with the next one.
        # 3) If nums[j] >= nums[j + 1], the sequence is not strictly increasing → return False.
        # 4) If the entire loop passes without returning False, return True (the subarray is increasing).
        for j in range(start, start + k - 1):
            if nums[j] >= nums[j + 1]:
                return False
        return True