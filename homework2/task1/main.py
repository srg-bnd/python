# Задание 1. Копирование содержимого одного файла в другой
# Создайте программу, которая копирует содержимое файла source.txt в новый файл destination.txt.

# Открываем оба файла одновременно
with open('../data/source.txt', 'r') as source_file, open('../data/destination.txt', 'w') as dest_file:
    # Читаем содержимое построчно и записываем в новый файл
    for line in source_file:
        dest_file.write(line)
