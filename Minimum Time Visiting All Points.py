class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if(len(points) < 2):
            return 0
        
        minSeconds = 0
        tempX = points[0][0]
        tempY = points[0][1]
        for i in range(1,len(points)):
            minSeconds = minSeconds + max(abs(points[i][1] - tempY),abs(points[i][0] - tempX))
            tempY = points[i][1]
            tempX = points[i][0]
        return minSeconds
        