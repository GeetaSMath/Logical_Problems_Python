from collections import deque

def bfs(graph, start):
    visited = set()         # Set to track visited nodes
    queue = deque([start])  # Queue to store nodes for traversal

    while queue:
        node = queue.popleft()
        print(node)  # Or perform any other operation on the node

        if node not in visited:
            visited.add(node)
            neighbors = graph[node]  # Get the neighbors of the current node

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
