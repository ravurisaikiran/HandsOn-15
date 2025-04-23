def bellman_ford(edges, vertices, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    for u, v, weight in edges:
        if dist[u] + weight < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return dist

if __name__ == "__main__":
    edges = [
        ('s', 't', 6), ('s', 'y', 7),
        ('t', 'x', 5), ('t', 'y', 8), ('t', 'z', -4),
        ('x', 't', -2),
        ('y', 'x', -3), ('y', 'z', 9),
        ('z', 's', 2), ('z', 'x', 7)
    ]
    vertices = ['s', 't', 'x', 'y', 'z']
    result = bellman_ford(edges, vertices, 's')
    print("Bellman-Ford result from 's':", result)
