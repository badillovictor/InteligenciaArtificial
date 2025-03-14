import numpy as np

neurons = [
    np.array([1,1,-1,-1]),
    np.array([1,-1,1,-1])
]
T = np.zeros([len(neurons[0]), len(neurons[1])])

for neuron in neurons:
    newMatrix = neuron * np.transpose(neuron)
    T += newMatrix

print(T)