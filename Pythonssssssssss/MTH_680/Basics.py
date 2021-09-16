'''
length
weight
base
distance
add codewords
dot product

matrix vector multiplication (native?)
transpose?
linearly independent?
'''


class Codeword:
    codeword: str
    length: int
    weight: int
    # base: int

    def __init__(self, codeword="") -> None:  # , base=2
        self.codeword = codeword
        self.length = len(codeword)
        self.weight = self.calculateWeight()
        # self.base = base

    def __str__(self):
        return self.codeword

    def calculateWeight(self) -> int:
        tempWeight = 0

        for char in self.codeword:
            if char != "0":
                tempWeight += 1

        return tempWeight

    def distanceTo(self, other: "Codeword") -> int:
        tempDistance: int = 0

        for x in range(0, len(self.codeword)):
            if self.codeword[x] != other.codeword[x]:
                tempDistance += 1

        return tempDistance

    def __add__(self, other: "Codeword") -> "Codeword":
        if other.length != self.length:
            raise RuntimeError("Cannot add Codewords of different lengths.")
        # if other.base != self.base:
        #     raise RuntimeError("Cannot add Codewords of different bases.")

        tempCodeword: str = ""
        for i in range(0, self.length):
            tempCodeword += str((int(self.codeword[i]) + int(other.codeword[i])) % 2)  # % self.base)

        return Codeword(tempCodeword)

    def add(self, other: "Codeword") -> "Codeword":
        return self + other

    def __mul__(self, other: "Codeword") -> "Codeword":
        if other.length != self.length:
            raise RuntimeError("Cannot multiply Codewords of different lengths.")
        # if other.base != self.base:
        #     raise RuntimeError("Cannot multiply Codewords of different bases.")

        tempCodeword: str = ""
        for i in range(0, self.length):
            tempCodeword += str((int(self.codeword[i]) * int(other.codeword[i])) % 2)  # % self.base)

        return Codeword(tempCodeword)  # , self.base)

    def dot(self, other: "Codeword") -> "Codeword":
        return self * other


def test():
    this = Codeword("1001")
    that = Codeword("0110")
    print(f"word: {this.codeword}")
    print(f"length: {this.length}")
    print(f"weight: {this.weight}")
    print(f"distance to {that.codeword}: {this.distanceTo(that)}")
