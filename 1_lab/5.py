import random
l = random.sample(range(1, 101), 20)
print(list(filter(lambda x: x % 2 == 0, l)))
print(list(filter(lambda x: x % 3 == 0, l)))
print(sum(l) / len(l))