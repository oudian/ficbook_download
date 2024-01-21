import os

# Путь к папке, где теперь находятся файлы
destination_folder = r'C:\Users\Dmitriy.DESKTOP-H28FQN8\Desktop\fb_s\fb_txt'

# Путь к файлу, в который записать список названий файлов
output_file_path = r'C:\Users\Dmitriy.DESKTOP-H28FQN8\Desktop\fb_s\file_list.txt'

# Получаем список файлов в папке
file_list = os.listdir(destination_folder)

# Фильтруем только файлы с расширением .txt
file_list = [filename for filename in file_list if filename.endswith('.txt')]

# Записываем список в текстовый файл
with open(output_file_path, 'w') as file:
    for filename in file_list:
        file.write(filename + '\n')

print(f'Список файлов записан в {output_file_path}')
