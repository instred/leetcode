from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.keytime = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keytime[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keytime[key]
        l, r = 0, len(values)-1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

if __name__ == "__main__":
    sol = TimeMap()
    a = ["set", "set", "get", "get", "set", "get", "get"]
    b = [["foo", "bar", 1], ["huj", "bar", 2], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

    for com, arg in zip(a,b):
        f = getattr(sol, com)
        f(*arg)