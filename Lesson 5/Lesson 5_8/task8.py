lst_inp1 = input()
lst_inp2 = input()
lst_abs1 = [int(d) for d in lst_inp1.split()]
lst_abs2 = [int(d) for d in lst_inp2.split()]
lst_res = [lst_abs1[i] + lst_abs2[i] for i in range(len(lst_abs1))]

print(*lst_res)

# # put your python code here
# inpt1 = [int(a) for a in input().split()]
# inpt2 = [int(a) for a in input().split()]
# res = [inpt1[i] + inpt2[i] for i in range(len(str))]
