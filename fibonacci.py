def get_fibonacci(n: int) -> int:
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(n - 1):
        temp = a + b
        a = b
        b = temp
    return b
