"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def occupation():
    age = abs(int(input('enter your age: ')))

    if 3 <= age <= 6:
        return 'kindergarten'
    elif 7 <= age <= 16:
        return 'school'
    elif 17 <= age <= 22:
        return 'university'
    elif 23 <= age <= 65:
        return 'work'
    else:
        return 'you were just born or enjoying retirement(ha-ha)'


def main():
    print(occupation())
    

if __name__ == "__main__":
    main()
