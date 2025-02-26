

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        aux = []
        k = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val: k += 1
            else: aux.append(nums[i])

        print(aux)
        print(nums)

        if len(nums) - k  == 0: return 0

        m = len(aux)
        j = 0
        for i in range(len(nums)):
            if nums[i] == val and j < m: 
                nums[i] = aux[j]
                j += 1

        print(nums)

        return len(nums) - k


s = Solution()
nums = [0,1,2,2,3,0,4,2]
nums = [1]
nums = [2,2,3]
val = 2
print(s.removeElement(nums, val))
