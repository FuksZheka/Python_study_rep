'''
Подвиг 6. На вход программе подается строка. Прочитайте эту строку и отобразите последние три ее символа.
Полагается, что строка гарантированно имеет длину не менее трех символов.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.2.6
'''

a = input()
print(a[len(a)-3:len(a)])