if __name__ == "__main__":
    input = input("Ingresa el vector separado por comas:\n")
    input = input.strip().split(",")
    if len(input) != 10:
        exit("No son 10 elementos")
    for i in range(len(input)):
        input[i] = int(input[i])
    input.sort()
    v1 = input[5:]
    v1 = v1[::-1]
    fibonacci = input[:5]
    v2 = [fibonacci.pop(0)]
    while len(fibonacci) > 0:
        v2.append(fibonacci.pop(0) + v2[-1])
    print("v1: " + str(v1))
    print("v2: " + str(v2))