# https://contest.yandex.ru/contest/28724/problems/C/


def check(a, b, c, aim):
    for i in range(3):
        if a[i] == b[i] == c[i] == aim:
            return True
    for i in (a, b, c):
        if i[0] == i[1] == i[2] == aim:
            return True
    if a[0] == b[1] == c[2] == aim:
        return True
    if a[2] == b[1] == c[0] == aim:
        return True


def solution(a, b, c):
    cnt_1, cnt_2 = 0, 0
    for i in (a, b, c):
        for z in range(3):
            if i[z] == 1:
                cnt_1 += 1
            if i[z] == 2:
                cnt_2 += 1
    
    if check(a, b, c, 1):
        if not check(a, b, c, 2) and cnt_1 == cnt_2 + 1:
            return 'YES'
        return 'NO'
    
    if check(a, b, c, 2):
        if cnt_2 == cnt_1:
            return 'YES'
        return 'NO'
    
    if cnt_1 == cnt_2 + 1 or cnt_1 == cnt_2:
        return 'YES'
    return 'NO'

"""
line1 = tuple(map(int, input().strip().split()))
line2 = tuple(map(int, input().strip().split()))
line3 = tuple(map(int, input().strip().split()))
print(solution(line1, line2, line3))
"""

solution((0,0,0), (0,0,0), (0,0,0)) == 'YES'
solution((0,0,1), (0,0,0), (0,0,0)) == 'YES'
solution((0,0,1), (0,2,0), (0,0,0)) == 'YES'
solution((0,0,0), (0,2,0), (0,0,0)) == 'NO'


 