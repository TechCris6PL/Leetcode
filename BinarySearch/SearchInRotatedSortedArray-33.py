# find target when array can be rotated
class Solution(object):
    def search(self,nums,target):
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # check if its in the left side
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target > nums[mid]: # if its greater than mid and right is greater than target then its must be on the other side
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
                    








test = Solution()
print(test.search([6,7,0,1,2],1))
print(test.search([4,5,6,7,8,0,1,2],8))
