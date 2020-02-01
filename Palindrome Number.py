class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        start = 0
        end = len(string) - 1
        flag = True
        while(start < end):
            if(string[start] != string[end]):
                flag = False
                break
            start += 1
            end -= 1
            
        return flag
        
		
		
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == int(str(x)[::-1])
		
