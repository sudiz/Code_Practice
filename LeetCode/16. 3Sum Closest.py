class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        temp=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):

            j,k=i+1,len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if abs(target-s)<abs(temp-target):
                    temp=s
                if s==target:
                    return target
                elif s>target:                 
                    k-=1
                else :               
                    j+=1
                
        return temp
