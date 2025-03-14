import numpy as np
import matplotlib.pyplot as plt
import DistanceMeasurements as DM


def InitialCentroids(dataset, k):
    indexes = np.random.choice(dataset.shape[0], size=k, replace=False)
    return dataset[indexes].copy()


def NextCentroids(clusters):
    newCentroids = []
    for cluster in clusters:
        if cluster:
            newCentroids.append(np.mean(cluster, axis=0))
        else:
            print('Cluster vacio, recalculando centroide...')
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
    kValues = [i for i in range(2, 15)]
    dataset = np.loadtxt(fname='dataset.csv', delimiter=',')
    dataset = dataset[:, 1:-1]

    iterationsPerK = []

    for k in kValues:
        print(f'Calculating for k={k}...')
        centroids = InitialCentroids(dataset, k)
        previousCentroids = None
        maxIterations = 1000
        iterations = 0

        while previousCentroids is None or not np.array_equal(centroids, previousCentroids) and iterations < maxIterations:
            previousCentroids = centroids.copy()

            clusters = [[] for _ in range(k)]
            classes = [GetClass(instance, centroids) for instance in dataset]

            for i, class_index in enumerate(classes):
                clusters[class_index].append(dataset[i])

            centroids = NextCentroids(clusters)
            iterations += 1

        iterationsPerK.append(iterations)

    plt.plot(kValues, iterationsPerK, marker='o')
    plt.xlabel('K')
    plt.ylabel('Iteraciones')
    plt.title('Iteraciones necesarias por cada K')
    plt.grid(True)
    plt.savefig('kmeans_iterations.png')