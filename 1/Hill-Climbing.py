

def hill_climbing(graph, start, goal, heuristic):
    path = [start]
    current = start
    cost = 0

    while current != goal:
        neighbors = graph[current]
        next_node = min(neighbors, key=lambda x: heuristic[x])
        path.append(next_node)
        cost += neighbors[next_node]
        current = next_node
        if current == goal:
            break

    print(f"Best Path: {path} \n cost {cost}")
    return path

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 1, 'E': 5},
    'C': {'A': 3, 'F': 4},
    'D': {'B': 1, 'G': 2},
    'E': {'B': 5, 'G': 3},
    'F': {'C': 4, 'G': 6},
    'G': {'D': 2, 'E': 3, 'F': 6}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}
hill_climbing(graph, 'A', 'G', heuristic)
