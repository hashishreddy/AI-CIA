from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start], 0)])  
    best_path = None
    min_cost = float('inf')

    while queue:
        node, path, current_cost = queue.popleft()

        if node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor], current_cost + cost))

    print(f"Best Path: {best_path} \n cost {min_cost}")
    return best_path
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 1, 'G': 2},
    'E': {'B': 5, 'G': 3},
    'F': {'C': 4, 'G': 6},
    'G': {'D': 2, 'E': 3, 'F': 6}
}
bfs(graph, 'A', 'G')
