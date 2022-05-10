﻿'''Дальше пойдут задачи на повторение и закрепление материала. Можно использовать любые техники,
 с которыми вы столкнулись в процессе обучения. И начнем мы с функций.

В Python существует строковая функция isdigit(). Эта функция возвращает True,
 если все символы в строке являются цифрами, и есть по крайней мере один символ, иначе — False.
 Напишите функцию с именем is_integer, которая будет расширять функциональность isdigit().
 При проверке строки необходимо игнорировать ведущие и замыкающие пробелы в строке.
 После исключения лишних пробелов строка считается представляющей целое число, если:

ее длина больше или равна одному символу
она целиком состоит из цифр
предусмотреть исключение, что, возможно, есть ведущий знак «+» или «-», после которого должны идти цифры'''


def is_integer(s):
    if len(s) == 0:
        return False
    else:
      try:
        s = int(s)
        if s%2 == 0 or s%2 == 1:
              return True
      except Exception:
          return False




