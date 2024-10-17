

def beam_search(graph, start, goal, heuristic, beam_width=2):
    queue = [(start, [start], 0)]
    best_path = None
    min_cost = float('inf')

    while queue:
        next_level = []

        for node, path, cost in queue:
            if node == goal and cost < min_cost:
                min_cost = cost
                best_path = path
                continue

            neighbors = sorted(graph[node].items(), key=lambda x: heuristic[x[0]])
            next_level.extend(
                (neighbor, path + [neighbor], cost + edge_cost) 
                for neighbor, edge_cost in neighbors
            )

        queue = sorted(next_level, key=lambda x: heuristic[x[0]])[:beam_width]

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

beam_search(graph, 'A', 'G', heuristic)
