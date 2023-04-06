class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num=[]
        for i in range(low,high+1):
            nm=i
            if i%10 > i//100:
                num3=i%10
                num1=i//100
                j=i//10
                if j%10 > j//10 and j%10 < i%10:
                   num2= j%10
                   if (num1==num2-1) and (num2==num3-1): 
                       num.append(nm)
        return num        
