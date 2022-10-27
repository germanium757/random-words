from typing import List
from RandomWordGenerator import RandomWord
import os

class CreateFiles:
    # | Объявляем объект класса с путём для создания файлов
    def __init__(self, file_path :str, name :str) -> None:
        try:
            os.mkdir(file_path)
        except Exception as e:
            pass
        self.file_path = file_path + '/' + name
        pass
    
    # | создаём файл с листом слов текста
    def fill_file_list(self, file_path :str, words :List[str]):
        with open(file_path, 'w') as text_writer:
            [text_writer.write(word + ' ') for word in words]
            pass
    
    # | создаём файл и добавляем каждое слов отдельно
    def fill_file_word(self, word_max_size, word_count :int, lines :bool):
        #| инициализируем класс рандомных слов
        rand_words = RandomWord(word_max_size, constant_word_size=False)
        
        if (lines):
            with open(self.file_path, 'a') as text_writer:
                [text_writer.write(rand_words.generate() + '\n') for i in range(word_count)]
        else:
            for i in range(word_count):
                with open(self.file_path, 'a') as text_writer:
                    text_writer.write(rand_words.generate() + ' ')