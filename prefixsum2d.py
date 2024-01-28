class PrefixSum2d:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])

        self.pref = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        
        for x in range(self.n):
            for y in range(self.m):
                self.pref[x + 1][y + 1] = (
                    self.pref[x][y + 1]
                    + self.pref[x + 1][y]
                    - self.pref[x][y]
                    + matrix[x][y]
                )

    def __repr__(self):
        return "\n".join([str(row) for row in self.pref])
    
    def sum(self, x1, y1, x2, y2):
        return (
            self.pref[x2][y2]
            - self.pref[x1][y2]
            - self.pref[x2][y1]
            + self.pref[x1][y1]
        )


def test_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    n = len(matrix)
    m = len(matrix[0])

    pref2d = PrefixSum2d(matrix)
    print(pref2d)

    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1 + 1, n + 1):
                for y2 in range(y1 + 1, m + 1):
                    naive_sum = sum([matrix[i][j] for i in range(x1, x2) for j in range(y1, y2)])
                    assert pref2d.sum(x1, y1, x2, y2) == naive_sum

