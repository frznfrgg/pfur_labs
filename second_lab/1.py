with open("data/data.txt") as f:
    l = list(map(int, f.readlines()))
    print(l)
    res = [sum(l), sum(l) / len(l), max(l), min(l)]
    print(res)

formats = ["Сумма: ", "Среднее: ", "Максимум: ", "Минимум: "]
with open("results/result.txt", "w") as f:
    for elem in zip(formats, res):
        f.write(str(elem[0]) + str(elem[1]) + "\n")