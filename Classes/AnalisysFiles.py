#| ИМПОРТ ФАЙЛОВ ПРОЕКТОВ
from Classes.Word import word

#| ИМПОРТ БИБЛИОТЕК
from typing import List

#| ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
def sort(list :List[word]):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if(list[i].word_lenght > list[j].word_lenght):
                list[i], list[j] = list[j], list[i]
    return list

class AnalisysFiles:
    def __init__(self, file_path :str) -> None:
        self.file_path = file_path
        self.word_types :List[word] = []
        self.sogl_count :int = 0
        self.glas_count :int = 0
        
    
    #| Перебор файла по строкам, затем анализ слова
    def Analise(self):
        with open(self.file_path, 'r') as file:
            while True:
                word_line = file.readline()
                if word_line == '':
                    break
                else:
                    self.__word_analis(word_line)
        self.word_types = sort(self.word_types)
        # self.print_result()
    
    
    def __word_analis(self, word_line :str):
        self.glas_count += word.get_glas_count(word_line)
        self.sogl_count += word.get_sogl_count(word_line)
        length :int = len(word_line) - 1
        for i in self.word_types:
            if(i.word_lenght == length): #| Если такая длина слова есть,
                i.inc_word()             #| то инкримируем количество этих самых слов
                return None
        self.word_types.append(word(length)) #| создаём новый тип слова с экземаляром класса слова, если такой длин нет
    
    
    #| ВЫВОД РЕЗУЛЬТАТОВ
    def print_result(self):
        #| ШАПОЧКА
        print('*'*60)
        print(f' Аналитика для файла {self.file_path}')
        print('*'*60)
        #| ВСЕГО СИМВОЛОВ
        amout_symbols :int = 0
        for word in self.word_types:
            amout_symbols += word.count * word.word_lenght
        print(f' 1. Всего символов --> {amout_symbols}')
        #| МАКС ДЛИНА СЛОВА
        print(f' 2. Максимальная длина слова --> {self.word_types[len(self.word_types) - 1].word_lenght}')
        #| МИН ДЛИНА СЛОВА
        print(f' 3. Минимальная длина слова --> {self.word_types[0].word_lenght}')
        #| СРЕДНЯЯ ДЛИНА СЛОВА
        amout_words :int = 0
        for word in self.word_types:
            amout_words += word.count
        # print(amout_words)
        print(f' 4. Средняя длина слова --> {round(amout_symbols/amout_words)}')
        #| КОЛИЧЕСТВО ГЛАСНЫХ
        print(f' 5. Количество гласных --> {self.glas_count}')
        #| КОЛИЧЕСТВО СОГЛАСНЫХ
        print(f' 6. Количество согласных --> {self.sogl_count}')
        #| ВЫВОД ПОВТОРОВ
        print(' 7. Количество повторений слов с одинаковой длиной:\n')
        [print(f'\t * {i.word_lenght} сим >> {i.count} повтор.') for i in self.word_types]
    