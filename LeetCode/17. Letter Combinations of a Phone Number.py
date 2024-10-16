class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        queue=['']
        if not digits:
            return []
        
        for i in digits:
            n=len(queue)
            for _ in range(n):
                temp=queue.pop(0)
                for j in hashmap[i]:
                    queue.append(temp+j)

        return queue
