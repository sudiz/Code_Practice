class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        if nums[0]>0 or nums[-1]<0:
            return []
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<=k and nums[j]==nums[j-1]: j+=1
                    while j<=k and nums[k]==nums[k+1]: k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                    while j<=k and nums[k]==nums[k+1]: k-=1
                else:
                    j+=1
                    while j<=k and nums[j]==nums[j-1]: j+=1
                
        return res
