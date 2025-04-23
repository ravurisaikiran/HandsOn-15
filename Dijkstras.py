import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist

if __name__ == "__main__":
    graph = {
        's': [('t', 10), ('y', 5)],
        't': [('x', 1), ('y', 2)],
        'x': [('z', 4)],
        'y': [('t', 3), ('x', 9), ('z', 2)],
        'z': [('s', 7), ('x', 6)],
    }

    result = dijkstra(graph, 's')
    print("Shortest distances from node 's':")
    for node, distance in result.items():
        print(f"{node} : {distance}")
