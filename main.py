import os
import utils
import player_class

# пути к json файлам, url и локальный
JSON_DATA_URL = 'https://www.jsonkeeper.com/b/SKWU'
DATA_PATH = os.path.join('data/words.json')


def main():
    """
    Основная функция
    """
    # сохраняем функцию 'load_random_word' в переменную
    basic_word = utils.load_random_word(JSON_DATA_URL, DATA_PATH)
    # знакомимся с игроком
    user_name = input("Введите имя игрока\n")
    if user_name == '' or user_name == ' ':
        user_name = "\033[43m\033[30mПустое место\033[00m"

    # объявляем экземпляр класса 'Player'
    player = player_class.Player(user_name)

    # приветствуем игрока, объявляем слово, озвучиваем условия выхода из игры
    print(f"Привет {player.name}\n"
          f"Составьте {basic_word.get_length_subword()} слов из слова \033[31m\"{basic_word.word}\"\033[00m.\n"
          f"Слова должны быть не короче 3 букв.\n"
          f"Чтобы закончить игру, угадайте все слова "
          f"или напишите стоп-слово: \033[35m\"schmetterling\"\033[00m или \033[35m\"флюгегехаймен\"\033[00m.\n"
          f"Поехали, ваше первое слово?")

    # запускаем цикл на проверку подслов пользователя
    while player.get_length_user_subword() != basic_word.get_length_subword():
        user_subword = input().strip().lower()
        if len(user_subword) < 3:
            print('слишком короткое слово')
        elif user_subword == "schmetterling" or user_subword == "флюгегехаймен":
            print('Повторяй это слово три раза в день как скороговорку, слабак .!.')
            break
        elif player.check_unique_user_subword(user_subword):
            print('уже использовано')
        elif not basic_word.is_correct(user_subword):
            print('неверно')
        else:
            player.add_user_subword(user_subword)
            print('верно')

    # Завершение игры с выводом статистики
    print(f"Игра завершена, вы угадали {player.get_length_user_subword()} слов!")


if __name__ == '__main__':
    main()
