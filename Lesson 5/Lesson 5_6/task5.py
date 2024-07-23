import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
n = len(lst_in)

for i in range(n):
    for j in range(n):
        if lst_in[i][j] != lst_in[j][i]:
            print("НЕТ")
            break
    else:
        continue
    break # выход из внешнего цикца
else:
    print('ДА')