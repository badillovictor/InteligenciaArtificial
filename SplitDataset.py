import numpy as np


def SplitDataset(dataset, sampleRatio):
    # Shuffle the dataset for randomness
    np.random.shuffle(dataset)

    # Calculate the split index
    split_index = int(len(dataset) * sampleRatio)

    # Split the dataset
    sample = dataset[:split_index]
    dataset = dataset[split_index:]

    # numpy doesn't have a pop function, I cry
    return sample, dataset
