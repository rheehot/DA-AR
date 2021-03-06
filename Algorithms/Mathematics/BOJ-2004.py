from sys import stdin
read = lambda : stdin.readline().rstrip()

def count(n, s):
    c = 0

    while n > 0:
        n = n // s
        c += n

    return c

N, M = map(int, read().split())

five = count(N, 5) - count(M, 5) - count(N-M, 5)
two = count(N, 2) - count(M, 2) - count(N-M, 2)

print(min(five, two))
