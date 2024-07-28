# lst_inp1 = input()
#
# lst_abs = [abs(float(d)) for d in lst_inp1.split()]
# lst_abs2 = []
# for i,d in enumerate(lst_abs):
#     if i % 2 == 0:
#         lst_abs2.append(d)
#
# print(*lst_abs2)

lst = [float(x) for i, x in enumerate(input().split()) if i % 2 == 0]
print(*lst)