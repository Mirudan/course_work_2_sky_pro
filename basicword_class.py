class BasicWord:
    def __init__(self, word, subwords):
        """
        Инициализация класса
        :param word: исходное слово
        :param subword: список подслов
        """
        self.subwords = subwords
        self.word = word

    def __repr__(self):
        """
        Метод для вызова полей класса
        :return: поля класса
        """
        return f"word = {self.word}, subwords = {self.subwords}"

    def is_correct(self, word):
        """
        Проверка введенного слова в списке подслов
        :return: bool
        """
        return word in self.subwords

    def get_length_subword(self):
        """
        Получаем длину списка подслов
        :return: длину списка в int значении
        """
        return len(self.subwords)
