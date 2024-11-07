class Solution:
    def isSubsequence(self,str1,str2):
        S = len(str1)
        T = len(str2)
        
        
        if str1 == "": return True
        if S > T: return False
        
        j = 0
        for i in range(T):
            if str2[i] == str1[i]:
                if j == S - 1:
                    return True
                j += 1
        return False
            
        