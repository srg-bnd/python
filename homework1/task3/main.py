# Задание 3. Создание собственных исключений
# Напишите программу, которая вычисляет сумму списка целых чисел.
# Создайте свои собственные классы исключений для обработки ситуаций, когда в списке есть хотя бы одно чётное или отрицательное число.
# Используйте оператор raise для генерации исключений.

class EvenNumberError(Exception):
    """Исключение, когда число чётное"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NegativeNumberError(Exception):
    """Исключение, когда число отрицательное"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def sum(numbers: list) -> int:
  sum = 0
  for x in numbers:
      if x < 0:
          raise NegativeNumberError(x)
      elif x % 2 == 0:
          raise EvenNumberError(x)
      else:
          sum += x

  return sum


print(sum([1,3, -1]))