a = int(input())
b = 0
f = [[[0] for j in range (a)] for i in range(a)]
for i in range(a):
    for j in range(a):
        b += 1
        if b <= a ** 2:
            f[i][j] = b
print(f)