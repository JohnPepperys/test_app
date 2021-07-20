def print_matrix(x, n, m):
    for i in range(n):
        for j in range(m):
            print(str(x[i][j]).ljust(3), end=' ')
        print()

# ----------------------------------------------------------- -
x = []
(n, m) = input().split()
n = int(n)
m = int(m)

for i in range(n):
    x.append([])
    for j in range(m):
        x[i].append(0)
#print_matrix(x, n, m)

i = 0
j = 0
flag = 0
for k in range(1, n*m+1):
    x[i][j] = k
    if flag == 0:
        j += 1
        if j == m or x[i][j] != 0:
            j -= 1
            i += 1
            flag += 1

    elif flag == 1:
        i += 1
        if i == n or x[i][j] != 0:
            i -= 1
            j -= 1
            flag += 1

    elif flag == 2:
        j -= 1
        if j == -1 or x[i][j] != 0:
            j += 1
            i -= 1
            flag += 1

    else:
        i -= 1
        if i == -1 or x[i][j] != 0:
            i += 1
            j += 1
            flag = 0

print_matrix(x, n, m)
