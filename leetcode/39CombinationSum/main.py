class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(k, target, path):
            if target == 0:
                result.append(list(path))
                return
            if target < 0:
                return
            for i in range(k, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result

s = Solution()
print(s.combinationSum([2,3,6,7], 7)) # [[2, 2, 3], [7]]



