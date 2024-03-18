# --------------------------------------------------
#	A simple perceptron.
# --------------------------------------------------

import numpy as np

def sigmoid(x: int):
	'''
		1 / (1 + np.exp(-x))
	'''
	return 1 / (1 + np.exp(-x))

def bpm(training_input, training_output, synaptic_weights):
	'''
		Back Propogation Method
	'''
	for _ in range(5000):
		input_layer = training_input
		output = sigmoid(np.dot(input_layer, synaptic_weights))

		error = training_output - output
		adjustments = np.dot(input_layer.T, error * (output * (1 - output)))

		synaptic_weights += adjustments
	return output

def run():
	training_input = np.array([[0,0,1],
							[1,1,1],
							[1,0,1],
							[0,1,1]])

	training_output = np.array([[0,1,1,0]]).T 

	np.random.seed(5)

	synaptic_weights = 2 * np.random.rand(3,1) - 1

	print("\n-Random init weights----")
	print(synaptic_weights)

	output = bpm(training_input, training_output, synaptic_weights)

	print("\n-Weights after learning--")
	print(synaptic_weights)

	print("\n-Results after learning--")
	print(output)
	print()

if __name__ == '__main__':
	run()
