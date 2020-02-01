class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        #Sum = 0
        #mul = 1
        #l = len(A)
        #print(l)
        #for i in range(-1,-(l+1),-1):
        #    Sum = Sum + (int(A[i]) * mul)
        #    mul = mul * 10
            
        #Sum = int (''.join(str(i) for i in A))
        #Sum = Sum + K
        #return (list(str(Sum)))
        return (list(str(int (''.join(str(i) for i in A)) + K)))
        '''A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A'''        
		
		
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return (list(str(int (''.join(str(i) for i in A)) + K))) 