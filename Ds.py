# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.


import csv
from random import randint
from functools import reduce
from pathlib import Path


class Validate:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name


    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)


    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно содержать только буквы')
        if not value.istitle():
            raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Student:
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _lessons = None


    def __init__(self, name, second_name, surname, lessons_file):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.lessons = lessons_file


    @property
    def lessons(self):
        return self._lessons


    @lessons.setter
    def lessons(self, lessons_file):
        self._lessons = {'lessons': {}}
        with open(lessons_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons['lessons'][row[0]] = {'assessments': [], 'test_results': [], 'average_test': None}
        self._lessons['middle_assessment'] = None
        self._lessons['middle_test'] = None


    def __call__(self, lesson, number, type_est: str = 'lesson'):
        if lesson not in self.lessons['lessons'].keys():
            raise AttributeError('Нет такого предмета')
        
        if type_est == 'lesson':
            if number < 2 or number > 5:
                raise ValueError('Оценка должна быть от 2 до 5')
            self.lessons['lessons'][lesson]['assessments'].append(number)
            self.lessons['middle_assessment'] = self.calculate_middle_estimate(self.lessons)

        elif type_est == 'test':
            if number < 0 or number > 100:
                raise ValueError('Оценка должна быть от 0 до 100')
            self.lessons['lessons'][lesson]['test_results'].append(number)
            self.lessons['lessons'][lesson]['average_test'] = reduce(lambda x, y: x + y, self.lessons["lessons"][lesson]["test_results"]) / len(self.lessons["lessons"][lesson]["test_results"])
            self.lessons['middle_test'] = self.calculate_middle_test(self.lessons)


    @staticmethod
    def calculate_middle_estimate(lessons):
        all_estimates = []
        [all_estimates.extend(lessons['lessons'][name]['assessments']) for name in lessons['lessons']]

        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)


    @staticmethod
    def calculate_middle_test(lessons):
        all_estimates = []
        [all_estimates.extend(lessons['lessons'][name]['test_results']) for name in lessons['lessons']]

        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)


    def __repr__(self):
        result = f'\nФИО студента = {self.name} {self.second_name} {self.surname}\nСредняя оценка \
по всем предметам = {self.lessons["middle_assessment"]}\nСредний бал по всем тестам = {self.lessons["middle_test"]}\n'
        result += '\nОценки по предметам:\n'

        for key, value in self.lessons['lessons'].items():
            result += f'{key} = {value["assessments"]}\n'
        result += "\nТесты по предметам:\n"

        for key, value in self.lessons['lessons'].items():
            result += f'{key} = {value["test_results"]}, ср.бал = {value["average_test"]}\n'

        return result


if __name__ == '__main__':
    student_1 = Student('Mikhail', 'Mikhailovich', 'Mikhailov', Path('lessons.csv'))

    student_1('русский язык', 4)
    student_1('русский язык', 5)
    student_1('математика', 3)
    student_1('математика', 4)
    student_1('история', 5)
    student_1('история', 4)
    student_1('химия', 5)
    student_1('химия', 3)
    student_1('физика', 4)
    student_1('физика', 3)
    student_1('информатика', 5)
    student_1('информатика', 5)

    student_1('русский язык', 91, 'test')
    student_1('русский язык', 80, 'test')
    student_1('математика', 60, 'test')
    student_1('математика', 76, 'test')
    student_1('история', 93, 'test')
    student_1('история', 78, 'test')
    student_1('химия', 89, 'test')
    student_1('химия', 61, 'test')
    student_1('физика', 75, 'test')
    student_1('физика', 69, 'test')
    student_1('информатика', 93, 'test')
    student_1('информатика', 98, 'test')

    print(student_1)


    student_2 = Student('Ivan', 'Ivanovich', 'Ivanov', Path('lessons.csv'))

    student_2('русский язык', randint(2, 5))
    student_2('русский язык', randint(2, 5))
    student_2('математика', randint(2, 5))
    student_2('математика', randint(2, 5))
    student_2('история', randint(2, 5))
    student_2('история', randint(2, 5))
    student_2('химия', randint(2, 5))
    student_2('химия', randint(2, 5))
    student_2('физика', randint(2, 5))
    student_2('физика', randint(2, 5))
    student_2('информатика', randint(2, 5))
    student_2('информатика', randint(2, 5))

    student_2('русский язык', randint(0, 100), 'test')
    student_2('русский язык', randint(0, 100), 'test')
    student_2('математика', randint(0, 100), 'test')
    student_2('математика', randint(0, 100), 'test')
    student_2('история', randint(0, 100), 'test')
    student_2('история', randint(0, 100), 'test')
    student_2('химия', randint(0, 100), 'test')
    student_2('химия', randint(0, 100), 'test')
    student_2('физика', randint(0, 100), 'test')
    student_2('физика', randint(0, 100), 'test')
    student_2('информатика', randint(0, 100), 'test')
    student_2('информатика', randint(0, 100), 'test')

    print(student_2)
