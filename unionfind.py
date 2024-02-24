class UnionFind:
    def __init__(self, nodes: int):
        self.parent = [i for i in range(nodes)]
        self.rank = [0] * nodes

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> None:
        px = self.find(x)
        py = self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def reset(self, x: int) -> None:
        self.parent[x] = x
        self.rank[x] = 0

