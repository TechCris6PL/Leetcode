class Solution(object):
    def longestPalindrom(self,s):
        def palindrom(left,right): # check odd and even palindrom, return it
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        MaxRn = s[0]
        for i in range(0,len(s)):

            odd = palindrom(i,i) # expand in both sides
            even = palindrom(i,i+1) # expand in both but let right be +1 more than i and left, for even
            if len(odd) > len(MaxRn):
                MaxRn = odd
            if len(even) > len(MaxRn):
                MaxRn = even 
        return MaxRn
test1 = Solution()
print(test1.longestPalindrom("aaaa"))

