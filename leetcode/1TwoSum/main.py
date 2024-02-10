

# TwoSum

class Solution(object):
    def TwoSum(self, nums, target) -> list:
        # Create a dictionary to store the index of each number
        num_dict = {}
        for i, num in enumerate(nums):
            num_dict[num] = i
        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the number
            diff = target - num
            # Check if the difference is in the dictionary and not the same index
            if diff in num_dict and num_dict[diff] != i:
                return [i, num_dict[diff]]
        return []


# Test cases
sol = Solution()
print(sol.TwoSum([2, 7, 11, 15], 9))  # [0, 1]