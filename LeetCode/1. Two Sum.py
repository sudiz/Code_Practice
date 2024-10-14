class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(0,len(nums)):
            hashmap[target-nums[i]]=i
        for j in range(0,len(nums)):
            if nums[j] in hashmap:
                if hashmap[nums[j]]!=j:
                    return [j,hashmap[nums[j]]]
