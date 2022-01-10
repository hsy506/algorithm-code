# 문제 출처 : https://www.acmicpc.net/problem/1439
# 뒤집기 문제, greedy
S = input()
while "11" in S:
    S = S.replace("11", "1")
while "00" in S:
    S = S.replace("00", "0")
print(min(S.count('0'), S.count('1')))
