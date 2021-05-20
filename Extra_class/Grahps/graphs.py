graph = [[0,1,1,0,0],
         [1,0,0,0,1],
         [1,0,0,0,1],
         [0,0,0,0,0],
         [0,1,1,0,0],
         
        ]

start = 0
visited = []
end = 3
def dfs(graph, start, end, visited):
    #print(start)
    visited.append(start)
    if start == end:
        return visited
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and i not in visited:
            res = dfs(graph,i,end,visited)
            if res:
                return visited

#print( dfs(graph, start, end, visited))


def bfs(graph, start, end):

    queue = [start]
    visited = []
    while queue != []:
        current = queue.pop(0)
        visited.append(current)
        if current == end:
            return visited
        for i in range(len(graph[current])):
            if graph[current][i] == 1 and i not in visited:
                queue.append(i)

print(bfs(graph, start,end))
