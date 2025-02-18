import pandas as pd
import numpy as np
import math
import SplitDataset as sd
import DistanceMeasurements as dm


# Function to calculate precision
def calculate_precision(confusionMatrix):
    truePositives = confusionMatrix[0, 0]
    falseNegatives = confusionMatrix[1, 1]
    return (truePositives + falseNegatives) / np.sum(confusionMatrix)


if __name__ == '__main__':
    # Pandas config
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')

    # Read csv
    rawFile = pd.read_csv("dataset.csv", header=None)

    # Remove the instance number column
    dataFrame = rawFile.iloc[:, 1:].values
    dataset = np.array(dataFrame)

    sampleRatios = [0.7, 0.8, 0.9]
    algorithms = ['Manhattan', 'Euclidean', 'NormalizedEuclidean', 'Cosine', 'Jaccard', 'SorenDice']

    # Initialize a DataFrame to store results
    results = pd.DataFrame(index=algorithms, columns=[
        "70:30 Confusion", "70:30 Precision",
        "80:20 Confusion", "80:20 Precision",
        "90:10 Confusion", "90:10 Precision"
    ])

    for i in range(3):
        # For each split
        for sampleRatio in sampleRatios:
            # Split the dataset
            sampleData, testData = sd.SplitDataset(dataset, sampleRatio)

            # Separate features and response column
            sampleFeatures = sampleData[:, :-1]
            sampleResponse = sampleData[:, -1]
            testFeatures = testData[:, :-1]
            testResponse = testData[:, -1]

            # Create the 6 confusion matrices
            confusionMatrices = {algorithm: np.zeros((2, 2)) for algorithm in algorithms}

            # For each testVector in the split
            for i, testVector in enumerate(testFeatures):
                distances = {algorithm: [] for algorithm in algorithms}

                # Calculate distances to each sampleVector
                for sampleVector in sampleFeatures:
                    distances['Manhattan'].append(dm.ManhattanDistance(testVector, sampleVector))
                    distances['Euclidean'].append(dm.EuclideanDistance(testVector, sampleVector))
                    distances['NormalizedEuclidean'].append(dm.NormalizedEuclideanDistance(testVector, sampleVector))
                    distances['Cosine'].append(dm.CosineDistance(testVector, sampleVector))
                    distances['Jaccard'].append(dm.JaccardDistance(testVector, sampleVector))
                    distances['SorenDice'].append(dm.SorenDiceDistance(testVector, sampleVector))

                # For each algorithm
                for algorithm in algorithms:
                    # Get the distances for this algorithm
                    dist = distances[algorithm]

                    # Find the 20% closest vectors
                    k = int(len(sampleFeatures) * 0.2)
                    closestIndices = np.argsort(dist)[:k]
                    closestResponses = sampleResponse[closestIndices]

                    # Count the majority class
                    majorityClass = 1 if np.sum(closestResponses == 1) > np.sum(closestResponses == 2) else 2

                    # Compare with the actual response
                    actualResponse = testResponse[i]
                    if actualResponse == 1 and majorityClass == 1:
                        confusionMatrices[algorithm][0, 0] += 1  # True Positive
                    elif actualResponse == 2 and majorityClass == 1:
                        confusionMatrices[algorithm][1, 0] += 1  # False Positive
                    elif actualResponse == 1 and majorityClass == 2:
                        confusionMatrices[algorithm][0, 1] += 1  # True Negative
                    elif actualResponse == 2 and majorityClass == 2:
                        confusionMatrices[algorithm][1, 1] += 1  # False Negative

            # Store results in the DataFrame
            for algorithm in algorithms:
                # Calculate the ratio key
                ratioKey = f"{int(sampleRatio * 100)}:{100 - int(sampleRatio * 100)}"

                # Convert the confusion matrix to a string for printing
                confusionMatrixStr = str(confusionMatrices[algorithm])
                results.loc[algorithm, f"{ratioKey} Confusion"] = confusionMatrixStr

                # Store the precision
                results.loc[algorithm, f"{ratioKey} Precision"] = calculate_precision(confusionMatrices[algorithm])

        # Display the results DataFrame
        print(results)