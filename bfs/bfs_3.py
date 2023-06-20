# Create a graph given in the above diagram.
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

# to print a BFS of a graph
def bfs(node):

    # mark vertices as False means not visited
    visited = [False] * (len(graph))

    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


# Driver Code
if __name__ == "__main__":
    bfs('A')
