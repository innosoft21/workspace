# 18. 4Sum
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

class Solution: 
    def fourSum(self, nums, target: int) : 
        res = [] 
        nums.sort() 
        for idx, value in enumerate(nums): 
            if idx > 0 and value == nums[idx-1]: 
                continue 
            left,right = idx +1,len(nums)-1 
            while left < right : 
                left2,right = left +1 ,len(nums) -1 
                while left2 < right : 
                    four_sum = value + nums[left] + nums[left2] + nums[right] 
                    if four_sum > target : 
                        right -=1 
                    elif four_sum < target: 
                        left +=1 
                    else: 
                        res.append([value,nums[left],nums[left2],nums[right]]) 
                        left2 +=1 
                        while nums[left2] == nums[left2-1] and left2 < right : 
                            left2 +=1 
                left +=1 
                while nums[left] == nums[left-1] and left < right : 
                    left +=1 
        return res

nums = [1,0,-1,0,-2,2]
target = 0
sol = Solution()
sol.fourSum(nums,target)