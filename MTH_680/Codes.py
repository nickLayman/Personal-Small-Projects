'''
2-to-5
repetition
Hamming
Even weight
Reed-Muller
Reed-Solomon
Cyclic
Huffman

length
dimension
minimum distance
base
'''

'''
Make these able to be generic, just give codewords list
Have the ability to define source word - codeword pairs
Use a dictionary?

Allow to define by either Generator or Parity Check (or dictionary)
'''

from Python.MTH_680 import Basics


class Code:
    parityCheck: [Basics.Codeword]
    generator: [Basics.Codeword]
    codewords: [Basics.Codeword]
    # TODO: add [n, k, d]_b with helper methods
    # length: int
    # dimension: int
    # minDistance: int
    # base: int

    def __init__(self, parityCheck=None, generator=None, codewords=None):  # , base=2
        self.parityCheck = parityCheck
        self.generator = generator
        self.codewords = codewords
        # self.length = calculateLength()
        # self.dimension = calculateDimension()
        # self.minDistance = calculateMinDistance()
        # self.base = base


def twoToFive() -> Code:
    tempList = ["00000", "01010", "10101", "11111"]
    newList = []
    for word in tempList:
        newList.append(Basics.Codeword(word))
    return Code(newList)


def repetition(n: int) -> Code:
    firstWord = ""
    secondWord = ""
    for i in range(n):
        firstWord += "0"
        secondWord += "1"
    return Code([Basics.Codeword(firstWord), Basics.Codeword(secondWord)])


# def hamming(n: int) -> Code:

# def evenWeight(length: int) -> Code:

# def reedMuller(??) -> Code:

# def reedSolomon(??) -> Code:

# def cyclic(??) -> Code:

# def huffman(text file??) -> Code:


