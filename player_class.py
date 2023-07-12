class Player:
    def __init__(self, name):
        """
        Инициализация класса
        :param name: имя игрока
        :param user_words: слова, использованные пользователем
        """
        self.user_words = []
        self.name = name

    def __repr__(self):
        """
        Метод для вызова полей класса
        :return: поля класса
        """
        return f"User(name = {self.name}, user_subwords = {self.user_words})"

    def get_length_user_subword(self):
        """
        Получаем длину списка использованных подслов
        :return: длину списка в int значении
        """
        return len(self.user_words)

    def add_user_subword(self, word):
        """
        Добавление подслова пользователя в список
        """
        self.user_words.append(word)

    def check_unique_user_subword(self, word):
        """
        Проверка использования ранее подслова пользователя
        :return: bool
        """
        return word in self.user_words
