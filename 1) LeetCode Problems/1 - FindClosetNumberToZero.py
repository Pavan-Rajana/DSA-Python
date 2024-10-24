class Solution:
    def findClosetNumberToZero(self,nums):
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest


sol = Solution()

print(sol.findClosetNumberToZero([-1,3,4,5,6,-19]))