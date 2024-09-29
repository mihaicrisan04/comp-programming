import Foundation

class Solution {
//  Dynamic programming approach
    // func jump(_ nums: [Int]) -> Int {
    //     var steps = [Int](repeating: 999999, count: nums.count)

    //     steps[0] = 0
    //     for i in 0..<nums.count {
    //         for j in 0...nums[i] {
    //             if i + j < nums.count {
    //                 steps[i + j] = min(steps[i] + 1, steps[i + j])
    //             }
    //         }
    //     }

    //     return steps[nums.count - 1]
    // }

    func jump(_ nums: [Int]) -> Int {
        var steps = 0
        var maxReach = 0
        var lastReach = 0

        for i in 0..<nums.count {
            if i > lastReach {
                lastReach = maxReach
                steps += 1
            }

            maxReach = max(maxReach, i + nums[i])
        }

        return steps 
    }
}

let s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump([2, 3, 0, 1, 4]))
