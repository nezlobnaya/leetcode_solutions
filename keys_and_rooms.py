class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        
        def dfs(room):
            visited.add(room)
            print(visited)
            for key in rooms[room]:
                print(key)
                if key not in visited:
                    dfs(key)
        dfs(0)
    
        return len(visited)==len(rooms)
                    
            