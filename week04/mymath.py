def factorial_iter(n):
    """
    팩토리얼 함수 (반복문)
    :param n:
    :return: 팩토리얼 결과값
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def factorial_recursive(n):
    """
    팩토리얼 함수 (재귀)
    :param n:
    :return: 팩토리얼 결과값
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)