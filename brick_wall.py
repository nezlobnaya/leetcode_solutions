class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = collections.Counter()
        rows = len(wall)
        
        
        for row in wall:
            offset  = 0
            for brick in row[:-1]:
                offset+=brick
                count[offset]+=1
        if len(count)==0:return rows
        output = rows - max(count.values())
        
        
        return output
        
    
        