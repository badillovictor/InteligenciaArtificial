import numpy as np
import DistanceMeasurements as DM
import matplotlib.pyplot as plt


def GetNextCombination(currentIndexes):
    pass

def NextCentroids(clusters):
    newCentroids = []
    for cluster in clusters:
        if cluster:
            newCentroids.append(np.mean(cluster, axis=0))
        else:
            #print('Cluster vacio, recalculando centroide...')
            newCentroids.append(dataset[np.random.choice(dataset.shape[0])].copy())
    return np.array(newCentroids)


def GetClass(instance, centroids):
    distance = float('inf')
    bestIndex = 0
    for i in range(len(centroids)):
        tempDistance = DM.CosineDistance(instance, centroids[i])
        if tempDistance > distance:
            bestIndex = i
            distance = tempDistance
    return bestIndex


if __name__ == '__main__':
    k = 3
    dataset = np.loadtxt(fname='dataset.csv', delimiter=',')
    dataset = dataset[:, 1:-1]

    combinationIndexes = [0, 1, 2]
    maxCombinations = 166667000
    dataset = dataset[:100]
    centroids = dataset[combinationIndexes].copy()

    for centroid in centroids:
        previousCentroids = None
        maxIterations = 200
        iterations = 0
        while previousCentroids is None or not np.array_equal(centroids,
                                                              previousCentroids) and iterations < maxIterations:
            previousCentroids = centroids.copy()

            clusters = [[] for _ in range(k)]
            classes = [GetClass(instance, centroids) for instance in dataset]

            for i, class_index in enumerate(classes):
                clusters[class_index].append(dataset[i])

            centroids = NextCentroids(clusters)
            iterations += 1
        print(centroids)