d = dict()
a = list(input().split())
for i in range(len(a)):
    tmp = list(a[i])
    key_i = ''.join(tmp[0:tmp.index('=')])
    value_i = int(''.join(tmp[tmp.index('=')+1:len(tmp)]))

    d[key_i] = value_i

print(*sorted(d.items()))