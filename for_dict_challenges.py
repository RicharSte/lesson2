
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

name_dict = {}
for names in students:
      name = names['first_name']
      if name in name_dict:
            name_dict[name] += 1
      else:
            name_dict[name] = 1

for students_name in name_dict:
    print(students_name, name_dict[students_name]) 
    
    
      

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

name_dict = {}
for names in students:
      name = names['first_name']
      if name in name_dict:
            name_dict[name] += 1
      else:
            name_dict[name] = 1

#вот это я чисто нагуглил, врядли бы сам до этого бы додумался
#я бы это делал гораздо длинее
most_common_name = sorted(name_dict.items(), key = lambda kv:(kv[1], kv[0]))

print(f'Самое частое имя среди учеников:', most_common_name[-1][0])

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
number = 1
name_dict = {}
for students in school_students:
    for names in students:
          name = names['first_name']
          if name in name_dict:
                name_dict[name] += 1
          else:
                name_dict[name] = 1
    most_common_name = sorted(name_dict.items(), key = lambda kv:(kv[1], kv[0]))
    print(f"Самое частое имя в классе {number}:", most_common_name[-1][0])
    number += 1
    
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

number = 0
while number < len(school):
  male = 0
  female = 0
  school1 = school[number]['class']
  for student in school[number]['students']:
        if is_male[student['first_name']] == False:
              female += 1
        else:
              male += 1
  print(f'В классе {school1} девочек -{female} шт, мальчиков - {male} штук')
  number += 1


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
male_dict = {}
female_dict = {}
number = 0

while number < len(school):
      for student in school[number]['students']:
            if is_male[student['first_name']] == True:
                  if school[number]['class'] not in male_dict:
                        male_dict[school[number]['class']] = 1
                  else:
                        male_dict[school[number]['class']] += 1
            else:
                  if school[number]['class'] not in female_dict:
                        female_dict[school[number]['class']] = 1
                  else:
                        female_dict[school[number]['class']] += 1
      number += 1

for_girls = sorted(female_dict.items(), key = lambda kv:(kv[1], kv[0]))
for_boys = sorted(male_dict.items(), key = lambda kv:(kv[1], kv[0]))


print(f'Больше всего мальчиков в классе {for_boys[-1][0]}')
print(f'Больше всего девочек в классе {for_girls[-1][0]}')
      

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a