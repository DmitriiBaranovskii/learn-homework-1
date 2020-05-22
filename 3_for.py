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
  grades = []

  for school_class in range(5):
      grades.append({'school_class': f'{school_class}a', 'scored' : [random.randrange(1, 5, 1) for i in range(5)]})

  print(grades)

  gpa_summ = 0
  gpa_class = 0

  for grade in grades:
      gpa_class = sum(grade['scored']) / len(grade['scored'])
      print(f'gpa for class {grade["school_class"]} is {gpa_class}')
      gpa_summ += gpa_class

  print(f'Total gpa is {gpa_summ/len(grades)}')
    
if __name__ == "__main__":
    main()
