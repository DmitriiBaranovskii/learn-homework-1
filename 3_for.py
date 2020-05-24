"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
import random

def main():

  grades = [{'school_class': f'{school_class}a', 'scored':[random.randrange(1, 5, 1) for i in range(5)]} for school_class in range(5)]

  gpa = {grade['school_class']: sum(grade['scored']) / len(grade['scored']) for grade in grades}
  gpa['Среднее по школе'] = sum(gpa.values())
  print(gpa)
    
if __name__ == "__main__":
    main()
