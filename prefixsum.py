class PrefixSum:
    def __init__(self, arr: list):
        self.pref = [0]
        for n in arr:
            self.pref.append(self.pref[-1] + n)

    def sum(self, i, j):
        return self.pref[j] - self.pref[i]


def test_arr():
    arr = [3, 2, 4, 1, 5]
    pref = PrefixSum(arr)

    # sum(arr[i:j]) == pref.sum(i, j)

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            assert sum(arr[i:j]) == pref.sum(i, j)

