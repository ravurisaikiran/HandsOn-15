import numpy as np

def floyd_warshall(weights):
    n = len(weights)
    dist = np.array(weights, dtype=float)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    graph = [
        [0,   3,   8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]
    ]
    result = floyd_warshall(graph)
    print("Floyd-Warshall result:")
    print(result)
