#given array of numbers, find all possible permutations (all numbers are distinct ints)
#we will use recursion for this
#base case: if len(nums) == 1, in which case, we return list of lists with
#one element by making a copy inside list (too slow, use nums[:] instead)

def permute(self, nums:list[int])->list[list[int]]:
    result = []
    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result
    