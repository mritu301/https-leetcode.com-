class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp2 = arr.copy()
        length = len(temp2)
        temp1 = []
        i = 0
        flag = False
        while i < length :
            if temp2[i] == 0 :
                flag = True
                temp1 = temp2[0:i] + [0] + temp2[i:(length - 1)]
                i += 2
                temp2 = temp1
            else :
                i += 1
        
        if flag :
            for index in range(length) :
                arr[index] = temp1[index]