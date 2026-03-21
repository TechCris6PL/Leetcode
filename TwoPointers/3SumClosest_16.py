class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        #result = []
        n = len(nums)
        closest = nums[0]+nums[1]+nums[2] 
        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:

                TheSum = nums[i] + nums[left] + nums[right]
                if (abs(TheSum-target) <  abs(closest-target)):
                    closest = TheSum 
                #result.append(TheSum)
                elif TheSum > target:
                    right -= 1
                elif TheSum < target:
                    left += 1
                else: # if closest == target
                    return closest  
        return closest
       
       #TheClosest = abs(result[0] - target)
        #Index_Of_Closest = 0
        #for z in result: 
        #    TempClosest = abs(z - target)
        #    if TempClosest < TheClosest:
        #        TheClosest = TempClosest 
        #        Index_Of_Closest = result.index(z)
        
        #return result[Index_Of_Closest]
        
test = Solution()
print(test.threeSumClosest([0,0,0],1))
