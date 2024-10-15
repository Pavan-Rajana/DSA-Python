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

# ! Example: s = "abcabcbb"
"""
# ? Third iteration (r = 2):
s[2] = 'c', which is not in sett.
Add 'c' to sett: sett = {'a', 'b', 'c'}.
Window length w = (2 - 0) + 1 = 3, longest = max(2, 3) = 3.

# ? Fourth iteration (r = 3):
s[3] = 'a', which is in sett (repeat detected).
Remove s[0] = 'a' from sett: sett = {'b', 'c'}, and move l = 1.
Add s[3] = 'a' to sett: sett = {'a', 'b', 'c'}.
Window length w = (3 - 1) + 1 = 3, longest = max(3, 3) = 3.

# ? Fifth iteration (r = 4):
s[4] = 'b', which is in sett (repeat detected).
Remove s[1] = 'b' from sett: sett = {'a', 'c'}, and move l = 2.
Add s[4] = 'b' to sett: sett = {'a', 'b', 'c'}.
Window length w = (4 - 2) + 1 = 3, longest = max(3, 3) = 3.
Continue this process until r = 7.

"""
