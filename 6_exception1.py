"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
dialog = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую', 'На каком языке?': 'Python'}

def ask_user():
# Не совсем понял где нужно раместить try внутри while True или снаружи
    try:
        while True:
            message = input('Задайте вопрос: ')
            for item in dialog:
                if message == item:
                    print(dialog.get(message))
                    break
                elif message != 'Пока':
                    print('Увы, я вас не понимаю')
                    break
            if message == 'Пока':
                break
    except (KeyboardInterrupt):
        print('\nПока!')
if __name__ == "__main__":
    ask_user()
