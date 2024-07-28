# a_inp = int(input())
# a = [[0 for i in range(a_inp)] for j in range(a_inp)]
# for i in range (len(a)):
#     for j in range(len(a[i])):
#         if i == j:
#             a[i][j] = 1
#
# [print(*i) for i in a]
#

n = int(input())

lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

[print(*i) for i in lst]