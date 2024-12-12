

class Solution:
    def outlier(self, nums):
        res = -1
        for i in range(len(nums)):
            suma = sum(nums[:i]) + sum(nums[i+1:])
            for j in range(len(nums)):
                if i == j: continue
                if suma - nums[j] == nums[j]: res = max(res, nums[i])
        return res

s = Solution()
print(s.outlier([4,1,3,16,2,10]))
print(s.outlier([4,1,2,1,10,3]))