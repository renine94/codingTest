# https://leetcode.com/problems/string-compression-ii/solutions/4468632/beats-100-users-c-java-python-javascript-dp-explained/
# DP 문제 아직 못품


from functools import lru_cache


class Solution:
    def compress(self, s: str) -> str:
        compressed = s[:1]
        count = 1
        for c in s[1:]:
            if compressed[-1] == c:
                count += 1
            else:
                if count != 1:
                    compressed += str(count)
                compressed += c
                count = 1
        else:
            if count != 1:
                compressed += str(count)
        
        return compressed
    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        compressed = self.compress(s)
        
        # K
        ...


ske_list = [
    # s, k, expected
    ('aaaaaaaaaaa', 0, 3),
    ('aaabcccd', 2, 4),
    ('aabbaa', 2, 2),
]

for s, k, expected in ske_list:
    result = Solution().getLengthOfOptimalCompression(s, k)
    assert result == expected





##############################################################################################
class Solution:
    @staticmethod
    def calc(v):
        if v <= 2: return v
        if v < 10: return 2
        if v < 100: return 3
        return 4
    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # dp[p][pk] = p 위치에 있을 때 pk 번 삭제 가능 횟수가 남아 있을 경우의 최소 경우의 숫자
        # dp[p][pk] = min(dp[i-1][pk-nocnt] + calc(cnt)) 
        # (0 <= i <= p, nocnt = i~p까지 s[p]가 아닌 문자들의 개수, cnt=i~p까지 s[p]인 문자들의 개수)
        @lru_cache(None)
        def go(p, pk):
            if p < 0:
                return 0
            
            ans = 10000
            nocnt = 0
            cnt = 0
            for i in range(p, -1, -1):
                if s[i] != s[p]:
                    nocnt += 1
                else:
                    cnt += 1
                if nocnt > pk:
                    break
                ans = min(ans, go(i-1, pk - nocnt) + self.calc(cnt))
            return ans                           
        
        return min([go(len(s)-1-pk, k-pk) for pk in range(k+1)])