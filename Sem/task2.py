# ✔ Доработаем задачу 1.
# ✔ Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


from collections import deque as deq
import json
from datetime import datetime as dt


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
    

    def __enter__(self):
        return self
    

    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = str(dt.now()).replace(':', '') + '.json'
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(str(self), f)


with Factorial(2) as f:
    print(f(5))
    print(f(7))
    print(f(2))
