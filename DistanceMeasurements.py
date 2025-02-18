import math


def ManhattanDistance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def EuclideanDistance(x, y):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))


def NormalizedEuclideanDistance(x, y):
    normX = math.sqrt(sum(a ** 2 for a in x))
    normY = math.sqrt(sum(b ** 2 for b in y))
    return math.sqrt(sum(((a / normX) - (b / normY)) ** 2 for a, b in zip(x, y)))


def CosineDistance(x, y):
    dotProduct = sum(a * b for a, b in zip(x, y))
    normX = math.sqrt(sum(a ** 2 for a in x))
    normY = math.sqrt(sum(b ** 2 for b in y))
    return 1 - (dotProduct / (normX * normY))


def JaccardDistance(x, y):
    intersection = sum(min(a, b) for a, b in zip(x, y))
    union = sum(max(a, b) for a, b in zip(x, y))
    return 1 - (intersection / union) if union != 0 else 1


def SorenDiceDistance(x, y):
    intersection = sum(a * b for a, b in zip(x, y))
    sum_x = sum(x)
    sum_y = sum(y)
    return 1 - (2 * intersection) / (sum_x + sum_y) if (sum_x + sum_y) != 0 else 1
