import heapq

def a_star(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, start, [start])]
    min_cost = float('inf')
    best_path = None
    visited = set()

    while queue:
        estimated, current, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            if current < min_cost:
                min_cost = current
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (current + cost + heuristic[neighbor], current + cost, neighbor, path + [neighbor]))

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

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

a_star(graph, 'A', 'G', heuristic)
