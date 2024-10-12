class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        
        res=[[1],[1,1]]
        last=res[-1]
        for i in range(3,numRows+1):
            temp=[1]*i
            for j in range(1,i-1):
                temp[j]=last[j]+last[j-1]
            res.append(temp)
            last=temp
        return res
