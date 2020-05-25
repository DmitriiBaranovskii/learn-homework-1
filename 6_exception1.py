"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
# Не совсем понял где нужно раместить try внутри while True или снаружи
    try:
        dialog = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'На каком языке?': 'Python'}
        message = ''
        while message != 'Пока':
            message = input('Задайте вопрос: ')
            if message in dialog:
                print(dialog[message])
            elif message != 'Пока':
                print('Увы, я вас не понимаю')
    except KeyboardInterrupt:
        print('\nПока!')
if __name__ == "__main__":
    ask_user()
