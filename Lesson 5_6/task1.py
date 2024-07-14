a = int(input())
for i in range(0, a):
    for j in range(0, a,+1):
        if j == a-1:
            print(5,end=' ')
        else:
            print(1,end=' ')
    print()

