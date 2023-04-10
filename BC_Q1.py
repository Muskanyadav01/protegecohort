class Solution:
    def addDigits(self, num: int) -> int:
      if num==0:
        return num
      else:  
         num1=num%10
         num2=num//10
         num3=num1+num2
         if num3>9 and num3<100:
           num4=num3%10
           num5=num3//10
           num6=num4+num5
           return num6
         else:
           return num3  
      
