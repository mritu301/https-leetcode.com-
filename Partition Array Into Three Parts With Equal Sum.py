class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        partitionSum = int (sum(A)/3)
        Sum = 0
        p = 0
        for i in range(len(A)):
            Sum += A[i]
            if Sum == partitionSum :
                Sum = 0
                p += 1
        
        if p == 3 :
            return True
        else :
            return False
        



class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
    	S = sum(A)
    	if S % 3 != 0: return False
    	g, C, p = S//3, 0, 0
    	for a in A:
    		C += a
    		if C == g:
    			if p == 1: return True
    			C, p = 0, 1
    	return False
		


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
    	return (lambda x,y: x in y and 2*x in y)(sum(A)//3,itertools.accumulate(A))