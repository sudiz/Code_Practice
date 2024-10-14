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
