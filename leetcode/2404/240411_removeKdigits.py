# https://leetcode.com/problems/remove-k-digits/submissions/1229098510/


###########################################################################
# 내 풀이1 (그냥 떠오르는대로 구현함 - 시간초과 발생)
###########################################################################
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        num = list(num)
        t = 0
        while t < k:
            for i in range(len(num) - 1):
                if num[i] < num[i + 1]:
                    num.pop(i + 1)
                    t += 1
                    break
                elif num[i] > num[i + 1]:
                    num.pop(i)
                    t += 1
                    break
        return str(int("".join(num)))


###########################################################################
# 풀이2 (시간초과로 인한 GPT에게 코드 최적화 요청)
###########################################################################
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0

        for digit in num:
            # 스택에서 작은 숫자를 제거하여 최소 숫자를 만듭니다.
            while stack and removed < k and stack[-1] > digit:
                stack.pop()
                removed += 1

            stack.append(digit)

        # 숫자를 제거하지 못한 경우, 남은 숫자 중에서 뒤에서부터 제거합니다.
        while removed < k:
            stack.pop()
            removed += 1

        # 앞부분의 0을 제거합니다.
        return "".join(stack).lstrip("0") or "0"


###########################################################################
# 풀이3 (다른사람 풀이 - 스택사용)
###########################################################################
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        remain = len(num) - k
        for c in num:
            while k and stk and stk[-1] > c:
                stk.pop()
                k -= 1
            stk.append(c)
        return "".join(stk[:remain]).lstrip("0") or "0"


num_k_expected = [
    ["1432219", 3, "1219"],
    ["10200", 1, "200"],
    ["10", 2, "0"],
    ["9", 1, "0"],
    ["112", 1, "11"],
]

for num, k, expected in num_k_expected:
    result = Solution().removeKdigits(num, k)
    assert result == expected
