

def branch_and_bound_greedy(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, start, [start])]
    best_path = None
    min_cost = float('inf')

    while queue:
        _, current_cost, node, path = queue.pop(0)

        if node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                queue.append((current_cost + cost + heuristic[neighbor], current_cost + cost, neighbor, path + [neighbor]))
                queue = sorted(queue, key=lambda x: x[0])

    print(f"Branch and Bound Greedy Best Path: {best_path} with cost {min_cost}")
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

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

branch_and_bound_greedy(graph, 'A', 'G', heuristic)
