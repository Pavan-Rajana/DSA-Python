class Solution:
    def lengthOfLongestSubstring(self,s):
        leftPointer = 0 
        longest = 0 
        sett = set()
        n = len(s)
        
        for rightPointer in range(n):
            while s[rightPointer] in sett:
                sett.remove(s[leftPointer])
                leftPointer+=1
                
            sett.add(s[rightPointer])
            
            """ Calculation of window length """
            window = (rightPointer - leftPointer) + 1 
            
            """ Comparison of longest and window """
            longest = max(longest,window)
        
        return longest
    
    
abs = "abcabcbb"

sol = Solution()
print(sol.lengthOfLongestSubstring(abs))    

