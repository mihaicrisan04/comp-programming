import Foundation

class Solution {
    // func canJump(_ nums: [Int]) -> Bool {
    //     var seen = [Bool](repeating: false, count: nums.count) // initialize an array of nums.count elements with false
    //     seen[0] = true

    //     for i in 0..<nums.count {       
    //         if seen[i] {
    //             for j in 0..<nums[i] {
    //                 seen[i + j] = true    
    //             }
    //         }
    //     }

    //     return seen[nums.count-1]
    // }

    func canJump(_ nums: [Int]) -> Bool {
        var maxReach = 0
        for i in 0..<nums.count {
            if i > maxReach {
                return false
            }
            maxReach = max(maxReach, i + nums[i])
        }
        return true
    }
}


let sol = Solution()
print(sol.canJump([2,3,1,1,4])) // true
print(sol.canJump([3,2,1,0,4])) // false