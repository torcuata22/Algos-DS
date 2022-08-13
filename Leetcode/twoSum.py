def twoSum(nums: list[int], target: int) -> list[int]:
    n=len(nums)
    t = target
    for i in range (0, n):
        for j in range(0, n):
            if nums[i] + nums[j] == t:
                print (j, i) 
            else:
                break
            
numbers = [1,2,3]
t=4
twoSum(numbers,t)
