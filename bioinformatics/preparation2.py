"""
По данным числам 1 <= n <= 30 и 1 <= w <= 10^9 и набору чисел 1 <= v1, v2... vn <= 10^9
найдите минимальное число k, для которого число w можно представить как сумму k чисел из набора v1, v2...vn. 
Каждое число из набора можно использовать сколько угодно раз. Известно, что в наборе есть единица 
и что для любой пары чисел из набора одно из них делится на другое. Гарантируется, что в оптимальном ответе число слагаемых не превосходит 10^4

Sample input:
4 90 1 2 10 50

Sample Output:
5 50 10 10 10 10
"""


""" 
Простейший жадный алгоритм, за счет того, что набор чисел попарно делится друг на друга
"""

def solution(w, seq):
    pos, res = 0, []
    while w != 0:
        if w >= seq[pos]:
            res.extend([seq[pos]] * (w // seq[pos]))
            w = w - seq[pos] * (w // seq[pos])
        else:
            pos += 1
    return res


_, w, *seq = map(int, input().strip().split())
seq.sort(reverse=True)
res = solution(w, seq)
print(len(res), ' '.join(map(str, res)))


assert solution(1, [1]) == [1]
assert solution(5, [1]) == [1, 1, 1, 1, 1]
assert solution(5, [2, 1]) == [2, 2, 1]
assert solution(6, [2, 1]) == [2, 2, 2]