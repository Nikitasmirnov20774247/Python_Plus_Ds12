# ✔ Создайте класс-генератор.
# ✔ Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# ✔ Если переданы два параметра, считаем step=1.
# ✔ Если передан один параметр, также считаем start=1.


class Factorial:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.result = 1
        for i in range(1, start):
            self.result *= i


    def __iter__(self):
        return self
    

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


    def __next__(self):
        if self.start < self.stop:
            self.result = self.factorial(self.start)
            self.start += self.step
            return self.result
        else:
            raise StopIteration
        

    def __str__(self):
        return self.result
        

for i in Factorial(9, 3, 3):
    print(i)
