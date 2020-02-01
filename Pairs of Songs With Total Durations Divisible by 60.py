class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        for i in range(len(time)):
            print("i = ", i)
            print("time[i] = ", time[i])
            for j in range(i+1,len(time)):
                print("\n j = ", j)
                print("time[j] = ", time[j])
                pairSum = time[i] + time[j]
                print("pairSum = ", pairSum)
                quotient, remainder = divmod(pairSum, 60)
                print("remainder = ", remainder)
                print("quotient = ", quotient)
                if(remainder == 0):
                    count += 1
                print("count = ", count)
                    
        return count
        
		
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        for i in range(len(time)):
            for j in range(i+1,len(time)):
                if (time[i] + time[j]) % 10 != 0 :
                    continue 
                elif (time[i] + time[j]) % 60 == 0 :
                    count += 1
                    
        return count
		
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import Counter
        
        count = 0
        
        freqCounts = Counter([x % 60 for x in time])
        
        if 30 in freqCounts:
            count += freqCounts[30] * (freqCounts[30] - 1) / 2
        
        if 0 in freqCounts:
            count += freqCounts[0] * (freqCounts[0] - 1) / 2
            del freqCounts[0]
            
        for i in range(1, 30):
            if i in freqCounts and (60-i) in freqCounts:
                count += freqCounts[i] * freqCounts[60-i]
                    
        return int (count)