# Задание 4. Копирование уникального содержимого одного файла в другой
# Создайте программу, которая считывает строки из файла input.txt,
#   сохраняет только уникальные строки и записывает их в новый файл unique_output.txt.

# Читаем все строки из входного файла
with open('../data/input.txt', 'r', encoding='utf-8') as file:
  lines = file.readlines()

# Преобразуем список в множество для получения уникальных строк
unique_lines = set(lines)

# Записываем уникальные строки в выходной файл
with open('../data/unique_output.txt', 'w', encoding='utf-8') as file:
  for line in unique_lines:
    file.write(line)
