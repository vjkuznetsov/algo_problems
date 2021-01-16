# https://leetcode.com/problems/wildcard-matching/
# leetcode 44
# hard

# NOT ACCEPTED
# TIME LIMIT EXCEEDED

import sys


def solution(s, p):

    def check(pos_w, pos_p):
        nonlocal max_w, max_p, s, p 
        if pos_p == max_p:
            return pos_w == max_w
        
        if p[pos_p] == '*':
            if pos_w == max_w:
                return check(pos_w, pos_p + 1)
            else:
                return check(pos_w, pos_p + 1) or check(pos_w + 1, pos_p + 1) or check(pos_w + 1, pos_p)
    
        else:
            if pos_w == max_w:
                return False
            
            if p[pos_p] == '?':
                return check(pos_w + 1, pos_p + 1)
            

            if p[pos_p] != s[pos_w]:
                return False
            
            return check(pos_w + 1, pos_p + 1)

    sys.setrecursionlimit(10**6)
    if len(p) != 0:
        np = p[0]
        for i in range(1, len(p)):
            if p[i] == '*' and np[-1] == '*':
                continue
            else:
                np += p[i]
    p = np

    max_w, max_p = len(s), len(p)
    return check(0, 0)


assert solution("aa", "a") == False
assert solution("aa", "*") == True
assert solution("cb", "?a") == False
assert solution("adceb", "*a*b") == True
assert solution("acdcb", "a*c?b") == False

solution('aaa', '***')

