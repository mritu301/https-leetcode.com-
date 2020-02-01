class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) < 2) :
            return False
        else :
            if(coordinates[0][0] == coordinates[1][0]) :
                for i in range(2, len(coordinates)-1):
                    if(coordinates[i][0] != coordinates[0][0]) :
                        return False
                return True
                        
            if(coordinates[0][1] == coordinates[1][1]) :
                for i in range(2, len(coordinates)-1):
                    if(coordinates[i][1] != coordinates[0][1]) :
                        return False
                return True
                        
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
            constant = coordinates[0][1] - (coordinates[0][0] * slope)
            print(slope)
            print(constant)
            for i in range(1, len(coordinates)):
                print(coordinates[i][1])
                y = (coordinates[i][0] * slope) + constant
                print(y)
                if(coordinates[i][1] != int (y)):
                    return False
        return True
        
		
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0] == coordinates[1][0]:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
            return True
        if coordinates[0][1] == coordinates[1][1]:
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != coordinates[0][1]:
                    return False
            return True
        
        
        for i in range(len(coordinates)-1):
            coordinates[i][0] = coordinates[i+1][0] - coordinates[i][0]
            coordinates[i][1] = coordinates[i+1][1] - coordinates[i][1]
        del coordinates[-1]
        
        
        t = coordinates[0][0]/coordinates[0][1]
        for i in range(1, len(coordinates)):
            if t*coordinates[i][1] != coordinates[i][0]:
                return False
        return True
        
		
		
