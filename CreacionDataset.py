import random

if __name__ == "__main__":
    with open(file="dataset.csv", mode="w", encoding="utf-8") as file:
        for i in range(1, 1001):
            instance = [random.randint(1, 10) for x in range(7)]
            instance.insert(0, i)
            instance.append(random.randint(1, 2))
            line = [str(j) for j in instance]
            file.write(",".join(line) + "\n")