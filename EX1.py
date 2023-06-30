# Graph representation using a dictionary

# Hi prveen i want more improvements
# Hi prveen i want more improvements
# Hi prveen i want more improvements
# Hi prveen i want more improvements
# Hi prveen i want more improvements
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS Algorithm
def bfs(graph, start, end):
    # Keep track of visited nodes
    visited = []
    # Create a queue for BFS
    queue = [start]

    while queue:
        # Dequeue a vertex from queue
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            # Get all adjacent nodes of the dequeued node
            for neighbor in graph[node]:
                queue.append(neighbor)

            # Check if the end node has been reached
            if node == end:
                return visited
    return visited

# DFS Algorithm
def dfs(graph, start, end, visited=[]):
    # Mark the source node as visited and print it
    visited.append(start)

    # Get all neighbors of the current node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, end, visited)

    # Check if the end node has been reached
    if start == end:
        return visited
    return visited

# Example outputs
print("BFS: ", bfs(graph, 'A', 'F')) # Output: BFS:  ['A', 'B', 'C', 'D', 'E', 'F']
print("DFS: ", dfs(graph, 'A', 'F')) # Output: DFS:  ['A', 'B', 'E', 'F', 'C', 'D']
