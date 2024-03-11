# https://leetcode.com/problems/custom-sort-string/solutions/4856417/python-3-4-lines-w-counter-filter-join-t-s-97-62/


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        temp = []
        for o in order:
            if o in s:
                cnt = s.count(o)
                temp.extend([o] * cnt)
                for _ in range(cnt):
                    s.remove(o)
            else:
                pass
        temp.extend(list(s))

        return "".join(temp)


order, s = "kqep", "pekeq"
expected = "kqeep"

result = Solution().customSortString(order, s)
assert result == expected
