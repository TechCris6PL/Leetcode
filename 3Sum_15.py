class Solution(object):
    def threeSum(self,nums):
        res = []
        nums.sort()
        for i in range(0,len(nums)-2): #0 to 3 for 6 element list
            #LOOk if i is the same as the previous one 
            if (i!=0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                #Look for duplicates
                #SECOND WAY
                #if (left != i+1 and nums[left] == nums[left-1]):
                    #left += 1
                    #continue                   
               #if (right != len(nums)-1 and nums[right] == nums[right+1]):
                    #right -= 1
                    #continue                 
              
                total = nums[i] + nums[right] + nums[left]
              
                if total == 0:

                    res.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left<right  and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res

s1= Solution()
print(s1.threeSum([0,0,0,0,0,1,1,2]))

