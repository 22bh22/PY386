#Задача №2937. Следующее и предыдущее
#https://informatics.msk.ru/mod/statements/view3.php?id=2296&chapterid=2937#1
#Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере.
#Пробелы, знаки препинания, заглавные и строчные буквы важны!
#Входные данные:
#Вводится целое число, по модулю не превосходящее 10000.
#Выходные данные:
#Выведите сначала фразу "The next number for the number ", затем введенное число, затем слово " is ",
#окруженное пробелами, затем формулу для следующего за введенным числа, наконец, знак точки без пробела.
#Аналогично в следующей строке для предыдущего числа. При необходимости используйте параметр вывода sep в языке Python.
x=int(input("Введите целое число\n"))
print(f"The next number for the number {x} is {x+1}.\nThe previous number for the number {x} is {x-1}.")
x=input()