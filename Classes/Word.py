# | Класс слова экземпляры которого будут хранить длину слова,
# | а также количество повторений
class word:
    def __init__(self, word_lenght) -> None:
        self.word_lenght = word_lenght
        self.count = 1
    
    def inc_word(self):
        self.count +=1
    
    # | СТАТИЧЕСКИЕ МЕТОДЫ, связанные с словом
    @staticmethod
    def get_glas_count(word :str) -> int:
        count :int = 0
        for c in word:
            for i in ['AEIOUY']:
                if c.upper() in i:
                    count +=1
        return count
    
    @staticmethod
    def get_sogl_count(word :str) -> int:
        count :int = 0
        for c in word:
            for i in ['BCDFGHJKLMNPQRSTVWXZ']:
                if c.upper() in i:
                    count +=1
        return count