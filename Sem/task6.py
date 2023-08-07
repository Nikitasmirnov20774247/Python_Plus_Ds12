# ✔ Изменяем класс прямоугольника.
# ✔Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


class Range:
    def __set_name__(self, owner, name):
        self.name = '_' + name


    def __get__(self, instance, owner):
        return getattr (instance, self.name)
    

    def validate(self, value):
        if value <= 0:
            raise ValueError('Значение должно быть больше нуля')
    

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)


class Rectangle:
    a = Range()
    b = Range()


    def __init__(self, a, b = None):
        self.a = a
        self.b = a if not b else b


    def get_lenght(self):
        return 2 * (self.a + self.b)


    def get_area(self):
        return self.a * self.b


    # @property
    # def a(self):
    #     return self._a


    # @property
    # def b(self):
    #     return self._b
    

    # @a.setter
    # def a(self, value):
    #     if value > 0:
    #         self._a = value
    #     else:
    #         raise ValueError('Значение должно быть больше нуля')
        

    # @b.setter
    # def b(self, value):
    #     if value > 0:
    #         self._b = value
    #     else:
    #         raise ValueError('Значение должно быть больше нуля')
        

r = Rectangle(10, 6)

print(r.a)
