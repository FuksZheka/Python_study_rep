'''Подвиг 9. На вход программе подается строка.
Необходимо прочитать эту строку и сформировать новую строку вида (без кавычек):
"Строка: <введенная строка>. Длина: <длина строки>".
Полученную строку вывести на экран.
P. S. В программе F-строки не использовать.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/3/3.1.9'''

# put your python code here
s = input()
print("Строка: " + s +". Длина: " +str(len(s)))