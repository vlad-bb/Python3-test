﻿'''Итоговая задача модуля два была на вычисление арифметического выражения. В задаче на повторение мы пойдем немного
другим путем и выполним похожую задачу, заодно закрепив знания по работе со строками и списками.
Разбиение строки на лексемы представляет собой процесс преобразования исходной строки в список из подстрок, называемых лексемами (token).

В арифметическом выражении лексемами являются: операторы, числа и скобки. Операторами у нас будут следующие символы: *, /, - и +.
Операторы и скобки легко выделить в строке — они состоят из одного символа и никогда не являются частью других лексем.
 Числа выделить сложнее, поскольку эти лексемы могут состоять из нескольких символов.
 Поэтому любая непрерывная последовательность цифр — это одна числовая лексема.

Напишите функцию, принимающую в качестве параметра строку, содержащую математическое выражение, и преобразующую ее в список лексем.
Каждая лексема должна быть либо оператором, либо числом, либо скобкой.

Пример:
  return re.findall(r'\d+|[\(\)+\-*/]', s)
"2+ 34 -5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
В целях упрощения считаем, что числа могут быть только целыми, и входная строка всегда будет содержать математическое выражение,
 состоящее из скобок, чисел и операторов.

Обратите внимание, что лексемы могут отделяться друг от друга разным количеством пробелов, а могут и не отделяться вовсе.
Пробелы не являются лексемами и в итоговый список попасть не должны'''
def token_parser(s):
    ss = s.replace(' ', '')
    token_list = []
    n = ''
    for i in ss:
        if i.isdigit():
            n += i
        if i in ('+', '-', '*', '/', '(', ')'):
            if n != '':
                token_list.append(n)
                n = ''
                token_list.append(i)
            else:
                token_list.append(i)
    if n != '':
      token_list.append(n)

    return token_list

# def token_parser(s):
#     ss= s.replace(' ', '')
#     str = ss.split('+-*/')
#     return str

print(token_parser('2+ 34 - 5 * 3'))
print(token_parser('(2+ 3) *4 - 5 * 3'))
