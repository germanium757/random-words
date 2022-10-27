#| ИМПОРТ ФАЙЛОВ ПРОЕКТА
import multiprocessing
from Classes.CreateFiles import CreateFiles
from Classes.AnalisysFiles import AnalisysFiles

#| ИМПОРТ БИБЛИОТЕК
from typing import List
from multiprocessing import Process
import random
import os

#| ОБЪЯВЛЕНИЕ ОБЩИХ ПЕРЕМЕННЫХ
list_process :List[Process] = []
word_max_size :int = 10

# | МЕТОДЫ СОЗДАНИЯ ФАЙЛОВ И ГЕНЕРАЦИИ СЛОВ 

# # | генерация листа слов, и заполнения файла листом
# def create_file(number :str):
#     # | Создание файла
#     create_files.fill_file_list(f'Process-{number}-{os.getpid()}.txt',                        # | ИМЯ ФАЙЛА 'Process-[номер]-[пид].txt'
#                                   rand_words.getList(random.randint(int(1E5), int(1E6))))  # | СОЗДАНИЕ СПИСКА в диапозоне от от ста тыс. до лимона
#     # | Анализ файла для экономии времени запускаем сразу после создания файла
    
# | упрощённый метод, вместо хранения в памяти дофига слов, храним одно
def create_file_word(number :str):
    print(f'Файл {number} создаётся....')
    rand = random.randint(int(1E5), int(1E6))
    create_files = CreateFiles('./files', f'Process-{number}-{os.getpid()}.txt')
    create_files.fill_file_word(word_max_size, rand, True)
    
def analise_files(file_name :str):
    analis = AnalisysFiles('./files/' + file_name)
    analis.Analise()
    analis.print_result()


if __name__ == '__main__':
    for i in range(multiprocessing.cpu_count()):
        # proc = Process(target=create_file, args=(str(i))) # | Создаём процесс, и отдаём номер текущей итерации
        proc = Process(target=create_file_word, args=(str(i + 1)),)
        proc.start()
        list_process.append(proc)
    [proc.join() for proc in list_process] # | Закрываем все процессы
    list_process.clear()                   # | Очищаем лист процессов

    for file_name in os.listdir('./files'):
        if (len(list_process) >= 8): break # | Защищаем мой бедненький компьютер от моей невнимательности
        proc = Process(target=analise_files, args=(file_name,))
        list_process.append(proc)
        proc.start()
    [proc.join() for proc in list_process] # | Закрываем все процессы
    
    

