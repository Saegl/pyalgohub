import heapq
from collections import defaultdict


# adjacency list of (dest, weight)
graph = {
    3: [(2, 2), (4, 6)],
    2: [(1, 5), (3, 2)],
    4: [(1, 9), (5, 2), (3, 6)],
    1: [(5, 1), (4, 9), (2, 5)],
    5: [(4, 2), (1, 1)],
}

def dijkstra(start, graph):    
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()
    while pq:
        aweight, a = heapq.heappop(pq)
        if a in visited:
            continue

        visited.add(a)
        for b, bweight in graph[a]:
            if aweight + bweight < dist[b]:
                dist[b] = aweight + bweight
                heapq.heappush(pq, (dist[b], b))

    return dist


def test_dijkstra():
    dist = dijkstra(1, graph)
    assert dist[1] == 0
    assert dist[2] == 5
    assert dist[3] == 7
    assert dist[4] == 3
    assert dist[5] == 1
    
