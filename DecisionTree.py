import SplitDataset as SD
import numpy as np
import pandas as pd


def ShannonEntropy(pX, pY, totalCases):
    if pX == 0 or pY == 0:
        return 0
    if pX == pY:
        return 2
    pX /= totalCases
    pY /= totalCases
    return -pX * np.log2(pX) - pY * np.log2(pY)


def PrintDataFrame(sampleRatio, variable, entropyTable, gain):
    print(f'Split: {sampleRatio}:{round(1-sampleRatio, 1)} - Variable {variable}, Ganancia: {gain}')
    df = pd.DataFrame(entropyTable, columns=['Atributo', 'Exitos', 'Fracasos', 'Casos', 'Entropia'])
    print(df)
    print('\n')


if __name__ == '__main__':
    sampleRatios = [0.7, 0.8, 0.9]
    dataset = []
    with open(file='datasetCualitativo.csv', mode='r') as csvfile:
        for line in csvfile:
            line = line.strip().split(',')
            dataset.append(line)
    header = dataset.pop(0)
    tablesGlobal = []
    for sampleRatio in sampleRatios:
        tablesPerSampleRatio = []
        sampleSplit, trainSplit = SD.SplitDataset(dataset, sampleRatio)
        yesCount = 0
        var1 = set()
        var2 = set()
        var3 = set()
        var4 = set()
        var5 = set()
        variables = [var1, var2, var3, var4, var5]
        for e in sampleSplit:
            if e[-1] == 'Si':
                yesCount += 1
            for i in range(len(variables)):
                variables[i].add(e[i])
        treeEntropy = ShannonEntropy(yesCount, len(sampleSplit) - yesCount, len(sampleSplit))
        for variableIndex in range(len(variables)):
            entropyTable = []
            gain = 0
            for attribute in variables[variableIndex]:
                positiveCount = 0
                negativeCount = 0
                for sample in sampleSplit:
                    if attribute == sample[variableIndex]:
                        if sample[-1] == 'Si':
                            positiveCount += 1
                        else:
                            negativeCount += 1
                totalCases = positiveCount + negativeCount
                attributeEntropy = ShannonEntropy(positiveCount, negativeCount, totalCases)
                attributeLine = [attribute, positiveCount, negativeCount, totalCases, attributeEntropy]
                gain += totalCases / len(sampleSplit) * attributeEntropy
                entropyTable.append(attributeLine)
            tablesPerSampleRatio.append([entropyTable, gain])
        tablesGlobal.append(tablesPerSampleRatio)
    for sampleRatioIndex in range(len(tablesGlobal)):
        for tableIndex in range(len(tablesGlobal[sampleRatioIndex])):
            PrintDataFrame(sampleRatios[sampleRatioIndex],
                           header[tableIndex],
                           tablesGlobal[sampleRatioIndex][tableIndex][0],
                           tablesGlobal[sampleRatioIndex][tableIndex][1])
