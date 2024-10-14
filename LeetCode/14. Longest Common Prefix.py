class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        end=strs[-1]
        res=''
        for i in range(0,min(len(end),len(first))):
            if end[i]==first[i]:
                res+=end[i];

            else:
                break;
        return res
# another version

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[j][i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
