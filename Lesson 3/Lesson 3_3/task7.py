'''
Подвиг 7. На вход программе подается строка (слаг).
Прочитайте ее и замените в ней все двойные дефисы (--) и тройные (---) на одинарные (-).
Подумайте, в какой последовательности следует выполнять эти замены.
Результат преобразования выведите на экран.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.3.7
'''
msg = input()
msg = msg.replace("--", "-")
msg = msg.replace("--", "-")
print(msg)

# Альтернативное решение
# s1 = input()
# while '--' in s1:
#     s1 = s1.replace('--','-')
# print(s1)