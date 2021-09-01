# https://contest.yandex.ru/contest/28724/problems/A/


import sys


def solution(a, b, c, d):
    if a == 0 and b == 0:
        return 'INF'
    # деление на ноль или деление с остатком
    if a == 0 or (b % a != 0):
        return 'NO'
    # знаменатель обращается в числитель
    if (c != 0) and (b // a == d // c):
        return 'NO'
    return -b // a


input_ = [int(line.strip()) for line in sys.stdin]
print(solution(*input_))


assert solution(1, 1, 2, 2) == 'NO'
assert solution(2, -4, 7, 1) == 2
assert solution(35, 14, 11, -3) == 'NO'



