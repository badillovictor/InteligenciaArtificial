import pandas as pd
import numpy as np
import SplitDataset as sp
import DistanceMeasurements as dm


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
    dataFrame = np.array(dataFrame)

    sampleRatios = [0.7, 0.8, 0.9]

    sampleData, testData = sp.SplitDataset(dataFrame, 0.7)
    sampleDF = pd.DataFrame(sampleData)
    testDF = pd.DataFrame(testData)

    # Pop the results column and store them for later    
    responseColumn = dataFrame[:, -1]
    dataFrame = dataFrame[:, :-1]

    # Ask the user for a 7 element vector
    inputVector = input("Ingresa el vector separado por comas:\n").strip().split(",")
    if len(inputVector) != 7:
        exit("Nope")

    # Convert the input to integers and np array
    inputVector = np.array([int(x) for x in inputVector])
    distances = []  # Distances vector

    # Calculate thex distance between the user vector and each instance
    for instance in dataFrame:
        manhattanDistance = distance.cityblock(inputVector, instance)
        euclideanDistance = distance.euclidean(inputVector, instance)
        # normalizedEuclideanDistance =
        cosineDistance = distance.cosine(inputVector, instance)
        distances.append([manhattanDistance, euclideanDistance])

    # Convert to np array for manipulation
    distances = np.array(distances)

    # Merge all the data
    combined_data = np.column_stack((dataFrame, responseColumn, distances))
    combined_df = pd.DataFrame(combined_data,
                               columns=[f"Valor {i}" for i in range(dataFrame.shape[1])] + ["Respuesta",
                                                                                              "D Manhattan",
                                                                                              "D Euclidiana"])

    # Re-convert to DataFrame for table format
    print(combined_df)