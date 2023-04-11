class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        indx=len(digits)-1
        digits[indx]=digits[indx]+1 
        for i in range(len(digits)):
                if len(str(digits[i]))==2: 
                    m=digits[i]//10
                    j=digits[i]%10
                    digits.append(m) 
                    digits.append(j)
                    digits.pop(0)    
        return digits
