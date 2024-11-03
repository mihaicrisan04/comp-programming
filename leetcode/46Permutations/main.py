
class Solution(object):
    def permute(self, nums):
        def back(k, x):
            if len(x) == len(nums):
                result.append(x[:]) # x[:] copy because x will be changed in the next
                return 
            for num in nums:
                if num not in x: # if condition()
                    x.append(num)
                    back(k+1, x)
                    x.pop()

        result = []
        back(0, [])
        return result

s = Solution()
print(s.permute([1, 2, 3]))