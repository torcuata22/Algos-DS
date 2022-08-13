#Given int. array, nums, and int. target, build expression out of nums
#by adding + and -  before each integer in nums and then concat ints.
#return number of different expressions you cna build that evaluate to target

def findTargetSumWays(nums:list[int], target:int)->int:
    dp = {} #cache (index, total) to track number of ways I can get there
    
    def backtrack(i, total):
        if i== len(nums):
             if total == target: 
                return 1
             else:
                 return 0
        if (i, total) in dp:
            return dp[(i,total)]
        
        dp[(i,total)] = (backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i]))
        
        return dp[(i,total)]


    