# https://contest.yandex.ru/contest/28724/problems/B/


def parrallel(x1, y1, x2, y2, x3, y3, x4, y4):
    if y2 == y1 and y4 == y3:
        return True
    if x2 == x1 and x4 == x3:
        return True
    if y2 == y1 or y4 == y3 or x2 == x1 or x4 == x3:
        return False
    if (y2 - y1) / (x2 - x1) == (y4 - y3) / (x4 - x3):
        return True
    return False


assert parrallel(1,1,2,1,-2,-1,-1,-1) == True
assert parrallel(0,0,0,1,5,-1,5,-3) == True
assert parrallel(1,1,2,2,-3,-3,-7,-7) == True


def solution(s):
    res = 0
    if parrallel(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]):
        res += 1
    if parrallel(s[0],s[1],s[4],s[5],s[2],s[3],s[6],s[7]):
        res += 1
    if parrallel(s[0],s[1],s[6],s[7],s[4],s[5],s[2],s[3]):
        res += 1
    if res == 2:
        return "YES"
    return "NO"


cnt = int(input())
for i in range(cnt):
    row_input = input()
    seq = tuple(map(int, row_input.strip().split()))
    print(solution(seq))


