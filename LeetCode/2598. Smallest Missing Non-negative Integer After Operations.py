class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            if nums[i]%value>=0:
                hashmap[nums[i]%value]+=1
            else:
                hashmap[value+(nums[i]%value)]+=1
            if nums[i]%value>=0:
                nums[i]=nums[i]%value+value*(hashmap[nums[i]%value]-1)
            else:
                nums[i]=value+(nums[i]%value)+value*(hashmap[value+(nums[i]%value)]-1)
     
        nums=list(set(nums))
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return i+1
