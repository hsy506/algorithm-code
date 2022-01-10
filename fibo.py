# https://www.acmicpc.net/problem/1003
# 피보나치 함수, dp

fibo0 = {}
fibo1 = {}
fibo0[0] = 1
fibo1[0] = 0
fibo0[1] = 0
fibo1[1] = 1
for i in range(0, 39):
    fibo0[i+2] = fibo0[i]+fibo0[i+1]
    fibo1[i+2] = fibo1[i]+fibo1[i+1]
T = int(input())
for i in range(0, T):
    N = int(input())
    print(fibo0[N], fibo1[N])
