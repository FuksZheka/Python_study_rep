'''
Подвиг 10. На вход программе подается строка, состоящая из названий городов, разделенных пробелом.
Необходимо прочитать эту строку и преобразовать так, чтобы названия городов шли через точку с запятой (без пробелов).
Результат  (строку) отобразите на экране.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.3.10
'''
a = input()
print(a.replace(" ",";"))

# скрипт для разделения строки по точкам (бонус)
# a = input().split('. ')
# for i in range(len(a)):
#     print(a[i])