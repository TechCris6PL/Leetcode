class Solution(object):
    def lengthOfLongestSubstring(self,s):
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        first = 0
        last = 0
        OverallMax = 1
        aktualne = set() # we will check if there is a duplicate (O(1))

        while last < len(s): 
            if s[last] not in aktualne: #then add to set to compare values and  expand the window 
                aktualne.add(s[last])
                last += 1
            
            else: # remove the first element to later check for next sequences
                aktualne.remove(s[first])
                if first <  len(s)-1 : # so we dont get out of index 
                    first += 1
                
                if OverallMax < last - first + 1: # If overallMax is less than current lenght of substring
                    OverallMax = last - first + 1
        if last - first> OverallMax:
            return last - first
        else:
            return OverallMax            
test = Solution()
print(test.lengthOfLongestSubstring("au"))


