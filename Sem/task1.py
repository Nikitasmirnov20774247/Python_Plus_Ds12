# ✔ Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# ✔ Экземпляр должен запоминать последние k значений.
# ✔ Параметр k передаётся при создании экземпляра.
# ✔ Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


from collections import deque as deq


class Factorial:
    def __init__(self, k):
        self.max_k = deq(maxlen=k)
        self.values = deq(maxlen=k)


    def __call__(self, value):
        result = 1
        for i in range(1, value+1):
            result *= i
        self.max_k.append(result)
        self.values.append(value)
        return self


    def __str__(self):
        return str({i:j for i, j in zip(self.values, self.max_k)})


f = Factorial(2)
print(f(5))
print(f(7))
print(f(3))
print(f(4))
print(f(2))
