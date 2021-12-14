from typing import List
from collections import defaultdict

# LeetCode / 332. Reconstruct Itinerary
class Solution:
    def dfs(self, idx: int) -> bool:
        if self.ticket_num == 0:
            return True

        for dest in range(self.n):
            if self.adj_matrix[idx][dest] > 0:
                # print(f'{self.vertices_dict[idx]} : {self.vertices_dict[dest]} + {self.adj_matrix[idx]} / {self.ticket_num}')
                self.result.append(self.vertices_dict[dest])
                self.ticket_num -= 1
                self.adj_matrix[idx][dest] -= 1
                if self.dfs(dest) == True:
                    return True
                
                self.result.pop()
                self.adj_matrix[idx][dest] += 1
                self.ticket_num += 1
        
        return False
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        chk = defaultdict(lambda: False)
        vertices = []
        for temp in tickets:
            if chk[temp[0]] == False:
                chk[temp[0]] = True
                vertices.append(temp[0])
            if chk[temp[1]] == False:
                chk[temp[1]] = True
                vertices.append(temp[1])    
        self.n = len(vertices)
        vertices.sort()
        self.vertices_dict = ["TEMP"] * self.n
        temp_vertices_dict = {}
        for idx in range(len(vertices)):
            self.vertices_dict[idx] = vertices[idx]
            temp_vertices_dict[vertices[idx]] = idx

        self.adj_matrix = [[0] * self.n for _ in range(self.n)]
        #print(self.adj_matrix)
        self.ticket_num = 0
        for temp in tickets:
            self.ticket_num += 1
            self.adj_matrix[temp_vertices_dict[temp[0]]][temp_vertices_dict[temp[1]]] += 1
        #print(self.adj_matrix)

        self.result = ["JFK"]
        self.dfs(temp_vertices_dict["JFK"])

        return self.result
        

tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(Solution().findItinerary(tickets))
