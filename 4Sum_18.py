class Solution(object):
    def fourSum(self,nums,target):
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        n = len(nums)
        for i in range(0,n-3):
            if (i>0 and nums[i] == nums[i-1]): # look for copies
                continue 
            for j in range(i+1,n-2):
                if (j > i+1 and nums[j] == nums[j-1]): # look for copies 
                    continue 
                left = j+1
                right = n  - 1
                while left < right:
                   
                    suma = nums[left] + nums[right] + nums[i] + nums[j] # sum 
                    if suma == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]]) # append to a list 
                        while right > left and nums[right] == nums[right-1]: # if a copy, skip 
                            right -= 1
                        while left < right and nums[left] == nums[left+1]: # if a copy, skip 
                            left += 1
                        left += 1 # change left and right so it can find a new result
                        right -= 1
                    elif suma > target:
                        right -= 1
                    else:
                        left += 1
        return result
test = Solution()
print(test.fourSum([-2,-1,-1,1,1,2,2],0))

