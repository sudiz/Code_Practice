class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(0,len(nums)-3):
            if nums[i]==nums[i-1] and i>0:
                continue
            for j in range(i+1,len(nums)-2):
                if nums[j]==nums[j-1] and j-1>i:
                    continue
                k,l=j+1,len(nums)-1
                while k<l:
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        l-=1
                        k+=1
                        while k<l and nums[l]==nums[l+1]: l-=1
                        while k<l and nums[k]==nums[k-1]: k+=1
                    elif nums[i]+nums[j]+nums[k]+nums[l]>target:
                        l-=1
                        while k<l and nums[l]==nums[l+1]: l-=1
                    else:
                        k+=1
                        while k<l and nums[k]==nums[k-1]: k+=1

        return res
