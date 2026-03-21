class Solution(object):
    def removeDuplicates(self,nums):
        j = 1 
        i = 0
        while j<len(nums):
            if nums[j] == nums[i]: # if they are the same move j to next object 
                j += 1
            else: 
                i += 1 # if they are both different , add 1 to i so it points to new object and let new i be the new object from j
                nums[i] = nums[j]
        return i+1
        

test1 = Solution()
print(test1.removeDuplicates([1,1,2]))
