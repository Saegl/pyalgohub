edges = [
    (1, 2, 5),
    (1, 3, 3),
    (1, 2, 7),
    (2, 4, 3),
    (2, 5, 2),
    (3, 4, 1),
    (4, 5, 2),
]


def bellman_ford(v, edges, start):
    """
    Calculate shortest distance from start to every node
    v: number of vertices
    edges: list of tuples (from, to, weight)
    """
    dist = [float('inf') for _ in range(v)]
    start = 1
    dist[start] = 0

    for _ in range(v - 1):
        for a, b, w in edges:
            dist[b] = min(dist[b], dist[a] + w)

    return dist


def test_bellman_ford():
    distances = bellman_ford(7, edges, 1)
    assert distances[5] == 6

