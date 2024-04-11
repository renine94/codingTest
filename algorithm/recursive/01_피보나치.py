from functools import lru_cache


@lru_cache(maxsize=3)
def fibo(n):
    """
    위 코드에서 functools.lru_cache 데코레이터를 사용하여 피보나치 함수를 메모이제이션하고 있습니다.
    메모이제이션은 함수의 결과를 캐시하여 이미 계산된 값은 다시 계산하지 않고 캐시된 값을 반환함으로써 실행 속도를 높이는 기법입니다.
    @lru_cache(maxsize=3)에서 maxsize=3은 최근에 계산된 3개의 결과만을 저장한다는 의미입니다.
    이는 피보나치 수열의 특성상 이전에 계산된 값들이 다음 계산에 재활용될 가능성이 높기 때문에 메모리를 적게 사용하면서도 효율적인 캐싱을 수행합니다.
    따라서 이러한 메모이제이션을 통해, 이전에 계산된 값을 다시 계산하지 않고 저장된 값을 바로 반환함으로써 실행 속도가 빨라지게 됩니다.
    """
    if n < 2:
        return n

    return fibo(n - 1) + fibo(n - 2)


for i in range(100):
    print(fibo(i))
