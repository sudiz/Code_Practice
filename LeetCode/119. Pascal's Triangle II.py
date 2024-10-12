class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=b=[1]
        while len(b)<rowIndex+1:
            a,b=b,[a+b for a,b in zip([0]+a,a+[0])]
        return b
