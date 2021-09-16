import random
import pickle
import sys
import math
import copy


# creates a node to be used in neural networks
class Node:
    def __init__(self):
        # whether the node is in the input layer
        self.inInputLayer = False

        # array of weights on connections to previous layer nodes
        self.weights = []

        # the bias that this node has
        self.bias = 0

        # this node's input
        # the dot product of the previous layer with self.weights
        self.input = 0

        # this node's output
        # function(input + bias) -> output
        self.output = 0

    def __str__(self):
        string = ''
        string += f"Weights: {str(self.weights)}\n"
        string += f"Bias: {str(self.bias)}\n"
        string += f"Input: {str(self.input)}\n"
        string += f"Output: {str(self.output)}"
        return string

    # sets whether the node thinks it is in the input layer
    # will not actually change the nodes position
    def setInInputLayer(self, b):
        self.inInputLayer = b

    # returns whether the node thinks it is in the input layer
    # does not check actual layer position
    def getInInputLayer(self):
        return self.inInputLayer

    # sets the bias of the node to the given value
    # function(input + bias) ==> output
    def setBias(self, val):
        self.bias = val

    # returns the current bias of the node
    # function(input + bias) ==> output
    def getBias(self):
        return self.bias

    # sets the input of the node to the given value
    # then recalculates the output
    # function(input + bias) ==> output
    def setInput(self, pInput):
        self.input = pInput
        self.recalculateOutput()

    # returns the input of the node
    def getInput(self):
        return self.input

    # used to (re)calculate output
    # separated off so that the function used can easily change
    # function(input + bias) ==> output
    # input is found at a network level
    def function(self, val):
        # # ReLU (Rectified Linear Unit) function
        # if val < 0:
        #     return 0
        # else:
        #     return val

        # sigmoid function
        return math.exp(val) / (math.exp(val) + 1)

    # recalculates the output of the node
    # function(input + bias) ==> output
    def recalculateOutput(self):
        self.output = self.function(self.input + self.bias)

    # directly sets output of the node
    # bipasses input and function
    # used only for input nodes
    # used so inverse functions and biases don't need to be considered
    # created when sigmoid was being used
    def setOutput(self, val):
        self.output = val

    # returns the output of the node
    def getOutput(self):
        return self.output


# creates many nodes, connects them, sets random weights and biases
class Network:
    def __init__(self, layers):
        # initialize an empty array of layers (an array of node arrays)
        self.layers = []
        self.makeMultipleLayers(layers)
        self.randomizeNetwork()

    # returns an array (a layer) with the given number of nodes
    # adds the given number of nodes to an array and returns that array
    # used in makeMultipleLayers
    def makeLayer(self, numNodes):
        # initialize an empty layer (array)
        layer = []

        # add numNodes nodes to the layer
        for x in range(0, numNodes):
            layer.append(Node())

        # return an array of numNodes nodes
        return layer

    # creates multiple layers of nodes
    # creates an array of node arrays
    # takes an array of integers as input
    # [4,2,2] ==> 3 layers with 4, 2, and 2 nodes each
    def makeMultipleLayers(self, ints):
        # for each input entry, append a layer with that many nodes
        for x in range(0, len(ints)):
            self.layers.append(self.makeLayer(ints[x]))

    # creates randomly weighted connections between consecutive layers
    def makeRandomWeights(self):
        # for all layers except the input layer, add weighted connections
        # connects current layer to previous layer
        # so input layer must be skipped
        for layerIndex in range(1, len(self.layers)):
            # calls the current layer 'clayer'
            clayer = self.layers[layerIndex]

            # calls the previous layer 'player'
            player = self.layers[layerIndex - 1]

            # for each node in clayer,
            # add weighted connections to all nodes in player
            for cnodeIndex in range(0, len(clayer)):
                # calls the current node 'cnode'
                cnode = clayer[cnodeIndex]

                # creates an empty array to become the weights array
                # calls the current array of weights 'cweights'
                cweights = []

                # for each node in player, add a weighted connection to cnode
                for pnodeIndex in range(0, len(player)):
                    # creates a random weight between -1 and 1
                    weight = (random.random() - 0.5) * 2

                    # appends the random weight to cweights
                    cweights.append(weight)

                # assigns cweights array to cnode
                cnode.weights = cweights

    # assigns random biases to every node
    def makeRandomBiases(self):
        # goes to every layer of nodes
        for layer in self.layers:
            # goes to every node in each layer
            for node in layer:
                # sets a random bias between -1 and 1 to each node
                node.setBias((random.random() - .5) * 2)

        # returns to input layer
        # and sets all biases to 0 so the actual inputs are used
        for node in self.layers[0]:
            node.setBias(0)

    def randomizeNetwork(self):
        self.makeRandomWeights()
        self.makeRandomBiases()

    # sets the inputs and outputs of the input layer
    # how any input is given to the network
    # takes in an array of floats as the input, calls this array 'floats'
    # each entry is assigned to the input and output of the corresponding node
    def setInitialLayerActivations(self, floats):
        # goes to every node in the input layer
        for index in range(0, len(self.layers[0])):
            # calls the current node 'cnode'
            cnode = self.layers[0][index]

            # sets input of cnode to the corresponding entry of floats
            # every node needs an assigned input or else errors are thrown
            cnode.setInput(floats[index])

            # sets output of cnode to the same corresponding entry of floats
            # bipasses input, bias, and function of the node
            cnode.setOutput(floats[index])

    # calculates all the other node inputs/outputs based on weights and biases
    def setAllOtherActivations(self):
        # goes to each non-input layer and calculates node activations
        for layerIndex in range(1, len(self.layers)):
            # calls the current layer 'clayer'
            clayer = self.layers[layerIndex]

            # calls the previous layer 'player'
            player = self.layers[layerIndex - 1]

            # goes to each node in clayer
            for cnodeIndex in range(0, len(clayer)):
                # calls the current node 'cnode'
                cnode = clayer[cnodeIndex]

                # creates placeholder int called 'cnodeInput'
                # and initializes it to 0
                cnodeInput = 0

                # for each node in player, adds its contribution to cnodeInput
                for pnodeIndex in range(0, len(player)):
                    # calls the current-in-use node
                    # in the previous layer 'pnode'
                    pnode = player[pnodeIndex]

                    # calculates the weighted output of pnode
                    # and adds it to cnodeInput
                    cnodeInput += cnode.weights[pnodeIndex] * pnode.getOutput()

                # sets cnode input to cnodeInput
                cnode.setInput(cnodeInput)

    def activateWithInput(self, pInput):
        self.setInitialLayerActivations(pInput)
        self.setAllOtherActivations()

    # used to manually check everything about the network
    # displays each node's layer, position, weights, input, bias, and output
    def checkValues(self):
        # goes to every layer
        for layerIndex in range(0, len(self.layers)):
            # goes to every node in each layer and displays its information
            for nodeIndex in range(0, len(self.layers[layerIndex])):
                # adds a blank line before every node's information
                print()

                # calls the current node 'node'
                node = self.layers[layerIndex][nodeIndex]

                # displays node's labeled information
                print("layer " + str(layerIndex) + " Node " + str(nodeIndex))
                print(node.__str__())
            # adds 2 blank lines after every layer finishes
            print()
            print()

    def tweak(self):
        for layer in self.layers:
            for node in layer:
                weights = node.weights
                for i in range(len(weights)):
                    if random.randint(0, 2):
                        weights[i] = (random.uniform(0.9, 1.1))*weights[i]
                    else:
                        weights[i] = (random.uniform(-1.1, -0.9)*weights[i])


def checkAccuracy(numerator, denominator, network):
    expectation = numerator % denominator == 0
    falseNode = network.layers[-1][0]
    trueNode = network.layers[-1][1]
    actual = [falseNode.output, trueNode.output]
    return expectation, actual


def cost(numerator, denominator, network):
    falseVal = network.layers[-1][0].output
    trueVal = network.layers[-1][1].output
    if numerator % denominator == 0:
        result = falseVal + (1 - trueVal)
    else:
        result = trueVal + (1 - falseVal)
    return result


def makeNumDen():
    numerator = random.randrange(sys.maxsize)
    numstring = bin(numerator)[2:]
    while len(numstring) < 63:
        numstring = "0" + numstring
    denominator = random.randrange(1, 32)
    denstring = bin(denominator)[2:]
    while len(denstring) < 5:
        denstring = "0" + denstring

    return numerator, denominator, numstring, denstring


def makeInputActivations(numstring, denstring):
    inputLayerActivations = []
    for bit in numstring:
        inputLayerActivations.append(int(bit))
    for bit in denstring:
        inputLayerActivations.append(int(bit))
    return inputLayerActivations


def makeManyNetworks(num):
    networks = []
    for i in range(num):
        networks.append(Network([68, 10, 2]))
    return networks


def main():
    numNets = 100
    numToKeep = 10  # must divide numNets
    rounds = 500
    networks = makeManyNetworks(numNets)
    numerator = 0
    denominator = 1
    numstring = ''
    denstring = ''

    for r in range(rounds):
        numerator, denominator, numstring, denstring = makeNumDen()

        inputLayerActivations = makeInputActivations(numstring, denstring)
        for net in networks:
            net.activateWithInput(inputLayerActivations)

        networks.sort(key=(lambda n: cost(numerator, denominator, n)))
        print(cost(numerator, denominator, networks[0]))
        # for net in networks:
        #     print(cost(numerator, denominator, net))
        # print()
        networks = networks[:numToKeep]

        for i in range(numToKeep):
            for t in range(numNets // numToKeep - 1):
                newNet = copy.deepcopy(networks[i])
                newNet.tweak()
                networks.append(newNet)

    numerator, denominator, numstring, denstring = makeNumDen()

    inputLayerActivations = makeInputActivations(numstring, denstring)
    for net in networks:
        net.activateWithInput(inputLayerActivations)

    networks.sort(key=(lambda n: cost(numerator, denominator, n)))

    print(cost(numerator, denominator, networks[0]))

    with open('Best.p', 'wb') as file:
        pickle.dump(networks, file)

    # with open('Test.p', 'rb') as file:
    #     test = pickle.load(file)


# main()


with open('Best.p', 'rb') as file:
    nets = pickle.load(file)

i = 1
for num in range(1, 50):
    numerator, denominator, numstring, denstring = makeNumDen()

    inputLayerActivations = makeInputActivations(numstring, denstring)
    nets[i].activateWithInput(inputLayerActivations)
    print(str(numerator % denominator == 0) + str(cost(numerator, denominator, nets[i])))

# well damn, it seems like ive made a lot of neural nets that just always
# tell me that any number does not divide another. its more common to say
# false so that's what they all do all the time and they're usually right
