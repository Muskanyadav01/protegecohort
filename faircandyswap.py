class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        answer=[]
        if len(aliceSizes)==len(bobSizes):
            for i in range(len(aliceSizes)):
                answer.append(aliceSizes[0])
            for j in range(len(bobSizes)):
                answer.append(bobSizes[0])
        else:
            answer.append(aliceSizes[0])
            answer.append(bobSizes[1])
        
        ans= [*set(answer)]   
        return ans
            
    
