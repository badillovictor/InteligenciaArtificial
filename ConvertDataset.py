import numpy as np


def CheckInterest(v):
    if v < 4:
        return 'Bajo'
    if v < 8:
        return 'Medio'
    return 'Alto'


def CheckAttendance(v):
    if v == 1:
        return 'Nula'
    if v < 9:
        return 'Irregular'
    return 'Regular'


def CheckParticipation(v):
    if v < 6:
        return 'Pasiva'
    return 'Activa'


def CheckAssignments(v):
    if v < 7:
        return 'Retraso'
    return 'Puntual'


def CheckActitude(v):
    if v < 5:
        return 'Negativa'
    return 'Positiva'


def CheckAnswer(v):
    return 'Si' if v == 1 else 'No'


if __name__ == '__main__':
    dataset = np.loadtxt(fname='dataset.csv', delimiter=',')
    newDataset = []
    with open(file='datasetCualitativo.csv', mode='w') as file:
        for row in dataset:
            newRow = [
                CheckInterest(row[1]),
                CheckAttendance(row[2]),
                CheckParticipation(row[3]),
                CheckAssignments(row[4]),
                CheckActitude(row[5]),
                CheckAnswer(row[-1])
            ]
            file.write(','.join(newRow) + '\n')