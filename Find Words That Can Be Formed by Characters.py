class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        
        def checkGoodWord(word: str, chars: str) -> bool:
            flag = True
            list1 = list(chars)
            for i in range(len(word)):
                if word[i] not in list1:
                    flag = False
                    break
                else:
                    list1.remove(word[i])
            return flag
        
        for i in range(len(words)):
            if(checkGoodWord(words[i], chars)):
                count += len(words[i])
        return count
		
		
		
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = 0
        dic = {x: 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
        for x in chars:
            dic[x] += 1
                
        for i in words:
            temp = {x: dic[x] for x in dic}
            flag = True
            for x in i:
                temp[x] -= 1
                if temp[x] < 0:
                    flag = False
                    break
                
            if flag:
                cnt += len(i)
        return cnt