class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        start = 0
        nums = sorted(nums)
        end = len(nums)
        for a in range(start, end - 3):
            for b in range(a+1, end - 2):
                c = b+1
                d = end - 1
                while(c < d):
                    temp = []
                    Sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if(Sum == target):
                        temp.append(nums[a])
                        temp.append(nums[b])
                        temp.append(nums[c])
                        temp.append(nums[d])
                        result.add(tuple(temp.copy()))
                        temp = temp.clear()
                        c += 1
                        d -= 1
                    elif(Sum > target):
                        d -= 1
                    else:
                        c += 1
                        
        return result        