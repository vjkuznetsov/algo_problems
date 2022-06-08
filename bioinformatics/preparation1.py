"""
Дано две строки T (длиной до 10^3) и P (длиной до 10^5). 
Подсчитайте количество точных вхождений второй строки в первую.
"""

"""
Первое решение - в лоб, за O(n^2)
Удивительно, но оно прошло
"""
def solution(t, p):
    pos, res = 0, 0
    while (cr := t.find(p, pos)) != -1:
        res += 1
        pos = cr + 1
    return res

t, p = input(), input()
print(solution(t, p))


assert solution("a", "0") == 0
assert solution("a", "a") == 1
assert solution("ba", "a") == 1
assert solution("baa", "a") == 2
assert solution("baba", "ba") == 2
assert solution("abababa", "aba") == 3