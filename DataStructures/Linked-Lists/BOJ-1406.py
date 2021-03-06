from sys import stdin
read = lambda: stdin.readline().rstrip()

left = list(read())
n = int(read())
right = []

for i in range(n):
    cmd = read().split()

    if cmd[0] == "L":
        if left:
            right.append(left.pop())

    elif cmd[0] == "D":
        if right:
            left.append(right.pop())

    elif cmd[0] == "B":
        if left:
            left.pop()

    elif cmd[0] == "P":
        left.append(cmd[1])

print(''.join(left) + ''.join(reversed(right)))
