
class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        first = second = float('inf')

        for num in nums:
            if num <= first: first = num
            elif num <= second: second = num
            else: return True

        return False



s = Solution()
print(s.increasingTriplet([1,2,3,4,5])) # True
print(s.increasingTriplet([5,4,3,2,1])) # False
print(s.increasingTriplet([2,1,5,0,4,6])) # True
