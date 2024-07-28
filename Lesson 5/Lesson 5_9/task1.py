import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst_in = [x
          for row in lst_in
          for x in row
         ]
lst_in.reverse()
print(*lst_in)
