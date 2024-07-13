number = list(input())
for i in range(2, len(number)):
    if number[i].isdigit():
        number[i] = 'x'


if "".join(number) == "+7(xxx)xxx-xx-xx":
    print('ДА')
else:
    print('НЕТ')
