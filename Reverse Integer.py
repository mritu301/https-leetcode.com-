class Solution:
    def reverse(self, x: int) -> int:
        def rev(x: int) -> int:
            result = 0
            #print("x = ", x, " and result = ", result)
            while(x > 0):
                ques, rem = divmod(x,10)
                result = (result* 10) + rem
                x = ques
                #print("x = ", x, " and result = ", result)
            return result
        
        negative = False
        if (x < 0):
            negative = True
            
        revInteger = rev(abs(x))
        
        if(revInteger > (pow(2,31) - 1)):
            revInteger = 0
        
        if(negative):
            revInteger = -1 * revInteger
            
        return revInteger
        