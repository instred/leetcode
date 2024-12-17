
from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(max_heap)
        result = []

        while max_heap:
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)
            result.append(char * use)

            if count > use and max_heap:
                next_char_neg, next_count = heappop(max_heap)
                result.append(chr(-next_char_neg))
                if next_count > 1:
                    heappush(max_heap, (next_char_neg, next_count - 1))
                heappush(max_heap, (char_neg, count - use))

        return "".join(result)
            
        


if __name__ == "__main__":
    s = "cczazcc"
    repeatLimit = 3
    s2 = "aababab"
    repeatLimit2 = 2
    sol = Solution()
    print(sol.repeatLimitedString(s, repeatLimit))
    print(sol.repeatLimitedString(s2, repeatLimit2))




