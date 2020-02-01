class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        start = 0
        nums = sorted(nums)
        end = len(nums)
        for i in range(start, end - 2):
            j = i+1
            k = end - 1
            while(j < k):
                temp = []
                Sum = nums[i] + nums[j] + nums[k]
                if(Sum == 0):
                    temp.append(nums[i])
                    temp.append(nums[j])
                    temp.append(nums[k])
                    result.add(tuple(temp.copy()))
                    temp = temp.clear()
                    j += 1
                    k -= 1
                elif(Sum > 0):
                    k -= 1
                else:
                    j += 1
                        
        return result
        