def fibo(n):
    """
    DP (동적프로그래밍)
    즉, 기억하며 풀기를 사용한 피보나치 수열 풀이 예시
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Test the function
for i in range(100):
    print(fibo(i))
