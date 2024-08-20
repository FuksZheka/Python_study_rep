import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
lst = [i.split('=') for i in lst_in]
for i in lst:
    d[int(i[0])] = i[1]
print(*sorted(d.items()))