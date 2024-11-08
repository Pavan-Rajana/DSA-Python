class Solution:
    def productExceptItself(self,nums):
        l_mul = 1
        r_mul = 1
        n = len(nums)
        
        l_arr = [0] * n
        r_arr = [0] * n
        
        for i in range(n):
            j = -i -1
            
            l_arr[i] = 1
            r_arr[j] = 1
            
            l_mul *= nums[i]
            r_mul *= nums[j]
            
        return (l * r for l, r in zip(l_arr,r_arr))
    
    #* Time: O(n)
    #* Space: O(n)