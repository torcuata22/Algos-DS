#Given an array rotate it to the right by k steps (k>0)
#When we rotate array we end up with two portions: portion 1 shifts to
#the end of the array, portion 2 (the last k elements)shifts to the
#beginning of the array.
#we can reverse teh array and then rotate the array in two stages:
#stage one reverses the first k elements and stage 2 reverses remainder
#ex: for k = 2 and nums=[1,2,3,4,5] --> revere whole array--> [5,4,3,2,1]
#[5,4] are the first k elements, we will rotate last
#[1,2.3] we will reverse first in place -->[4,5,1,2,3]
#also, we need to normalize k in case it is > than len(nums), so k=k%len(nums)

class Solution:
    def rotate(self, nums:list[int])->None:
        k=k%len(nums) 
        l,r = 0, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r = l+1, r-1
            
        l,r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l,r = l+1, r-1
            