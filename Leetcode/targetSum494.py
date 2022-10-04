#Given int. array, nums, and int. target, build expression out of nums
#by adding + and -  before each integer in nums and then concat ints.
#return number of different expressions you cna build that evaluate to target
from collections import defaultdict

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
    
#METHOD 2 (no caching):

def findTargetSumWays(self, nums, target):
    dp = defaultdict(int)
    dp[0] = 1 #initialize at 1 so nums array has something to compare to


    for num in nums:
        new_dp = defaultdict(int)
        for n in dp:
            new_dp[n+num] += dp[n]
            new_dp[n-num] += dp[n]

        dp = new_dp


    return dp[target]


    