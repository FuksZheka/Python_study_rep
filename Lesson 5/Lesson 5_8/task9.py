n = [i for i in input().split()]
year = [int(n[i]) for i in range(1, len(n), 2)]
town = [str(n[i]) for i in range(0, len(n), 2)]

res = []
for i in range(len(town)):
    res.append([town[i], int(year[i])])
print(res)

