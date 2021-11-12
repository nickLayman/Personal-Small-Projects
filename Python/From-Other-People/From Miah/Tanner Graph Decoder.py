## Tanner graph

import MiahNum
import random as rd

## Workflow is p much as follows:
## First we set up a Tanner Graph 'T' (near bottom lines)
## input is a Parity Check matrix (rows, columns, array)
## The check and variable nodes are formed in Tanner.__init__
## 
## Then we call T.decode(*) with a word or words as input
## The input has to be a string, otherwise python gets fucky
## 
## decode() then sets up the variable nodes' values 
## then we enter a loop where we evaluate each Cnode
## with Cnode.eval(). This then calculates the sum of
## each Vnode's (connected to it) values and takes this
## sum as its value. 
## 
## If the sum of each Cnode's value is 0, we break out of the loop
## and add the word to a string which essentially keeps a list of the
## words we have decoded (if multiple words were given).
##
## Otherwise the Cnodes send their feedback to the Vnodes
## and the Vnodes take on new values based on that feedback.
## Then the loop repeats.
##
## When all words have either failed or been decoded decode() returns
## the string which had kept track of those words.

## P.S. >> I am super sorry for anyone who tries to decpiher this.


class Vnode:
    def __init__(self,index):
        self.name = "v{}".format(index)
        self.index = index
        self.val = None
        self.vals = []
        self.q = None
        self.Q = None
        self.rs = []
        self.P = None
    def reval(self):
        """Uses inputs from Check layer to determine
        if a change to self.val needs to be made"""
        self.val = round(sum(self.vals)/len(self.vals))
        self.vals = [self.val]

class Cnode:
    def __init__(self,*vnodes, name='c'):
        self.val = 0
        self.vnodes = {}
        for i in vnodes:
            self.vnodes[i] = None
        self.name = name
    def eval(self):
        "Tests for errors in the recieved word"
        for i in self.vnodes:
            self.vnodes[i] = i.val
        self.val = sum(self.vnodes.values())%2
        return self.val
    def send(self):
        for i in self.vnodes:
            i.vals.append((self.val-i.val)%2)

class Tanner:
    def __init__(self,n,m,*array,**nodes):
        self.H = MiahNum.Matrix(n,m,*array)
        self.vnodes = [Vnode(i) for i in range(m)]
        self.cnodes = [Cnode(*(v for v in self.vnodes
                             if self.H.ind(i,v.index)!=0),name='c{}'.format(i))
                       for i in range(n)]
    def hdecode(self,*words,loops=20):
        output = {}
        for word in words:
            for i,j in zip(self.vnodes,word):
                i.val = int(j)
                i.vals = [int(j)]
            for i in range(loops):
                if sum(c.eval() for c in self.cnodes)==0:
                    word = "".join(str(i.val) for i in self.vnodes)
                    output[word] = 'good'
                    break
                else:
                    if i == 19:
                        word = "".join(str(i.val) for i in self.vnodes)
                        output[word] = 'failed'
                    for i in self.cnodes:
                        i.send()
                    for i in self.vnodes:
                        i.reval()
        return output
    def __repr__(self):
        return "".join("Cnode{}\n".format(tuple(j.index for j in i.vnodes.keys())) for i in self.cnodes)
    def sdecode(self,*words,loops=20,P=.9):
        output = ""
        for word in words:
            #set P_i, initial .Q vals
            for i,j in zip(self.vnodes,word):
                i.val = int(j)
                i.Q = i.val
            for i in self.vnodes:
                i.P = P if i.val==1 else 1-P
                #set var nodes .q tuple of (1-P_i,P_i)  
                i.q = (1-i.P,i.P)
            #check
            check_word = MiahNum.Matrix(len(self.vnodes),1,*tuple(i.Q for i in self.vnodes))
            result = self.H*check_word
            if result%2 == MiahNum.Matrix.zero(len(self.cnodes),1):
                output += "".join(tuple(f"{i}" for i in check_word.array))+" "
                continue
            if result%2 == MiahNum.Matrix.zero(len(self.cnodes),1):
                print("oof")
            for counter in range(loops):
                #set var nodes .r tuple of (r()),r(1))
                for j in self.cnodes:
                    for i in j.vnodes:
                        r = 0.5+0.5*MiahNum.prod(list(1-2*k.q[1] for k in j.vnodes if k is not i))
                        i.rs += [(r,1-r)]
                #set var nodes .Q tuple of (Q(0),Q(1))
                for i in self.vnodes:
                    p = (1-i.P)*MiahNum.prod(list(t[0] for t in i.rs))
                    q = i.P*MiahNum.prod(list(t[1] for t in i.rs))
                    K = 1/(p+q)
                    i.Q = 0 if max(K*p,K*q)==K*p else 1 
                #check
                check_word = MiahNum.Matrix(len(self.vnodes),1,*tuple(i.Q for i in self.vnodes))
                result = self.H*check_word
                if result%2 == MiahNum.Matrix.zero(len(self.cnodes),1):
                    output += "".join(tuple(f"{i}" for i in check_word.array))+" "
                    break
                #set var nodes .q tuple of (q(0),q(1))
                for i in self.vnodes:
                    p = (1-i.P)*MiahNum.prod(list(t[0] for t in i.rs if t is not i))
                    q = i.P*MiahNum.prod(list(t[1] for t in i.rs if t is not i))
                    K = 1/(p+q)
                    i.q = (K*p,K*q) 
                #repeat
            else :
                output += "".join(tuple(f"{i.Q}" for i in self.vnodes))+"? "          
        return output








## Find a way to generate all 1-bit errors 
    
info = (4,8,
        1,0,1,1,0,1,0,0,
        1,0,0,1,1,1,0,0,
        0,1,0,0,1,0,1,1,
        0,1,1,0,0,0,1,1)
T = Tanner(*info)

words = ['00000000', '00000001', '00000010', '00000011', '00000100', '00000101', '00000110', '00000111', '00001000', '00001001', '00001010', '00001011', '00001100', '00001101', '00001110', '00001111', '00010000', '00010001', '00010010', '00010011', '00010100', '00010101', '00010110', '00010111', '00011000', '00011001', '00011010', '00011011', '00011100', '00011101', '00011110', '00011111', '00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111', '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', '01011000', '01011001', '01011010', '01011011', '01011100', '01011101', '01011110', '01011111', '01100000', '01100001', '01100010', '01100011', '01100100', '01100101', '01100110', '01100111', '01101000', '01101001', '01101010', '01101011', '01101100', '01101101', '01101110', '01101111', '01110000', '01110001', '01110010', '01110011', '01110100', '01110101', '01110110', '01110111', '01111000', '01111001', '01111010', '01111011', '01111100', '01111101', '01111110', '01111111', '10000000', '10000001', '10000010', '10000011', '10000100', '10000101', '10000110', '10000111', '10001000', '10001001', '10001010', '10001011', '10001100', '10001101', '10001110', '10001111', '10010000', '10010001', '10010010', '10010011', '10010100', '10010101', '10010110', '10010111', '10011000', '10011001', '10011010', '10011011', '10011100', '10011101', '10011110', '10011111', '10100000', '10100001', '10100010', '10100011', '10100100', '10100101', '10100110', '10100111', '10101000', '10101001', '10101010', '10101011', '10101100', '10101101', '10101110', '10101111', '10110000', '10110001', '10110010', '10110011', '10110100', '10110101', '10110110', '10110111', '10111000', '10111001', '10111010', '10111011', '10111100', '10111101', '10111110', '10111111', '11000000', '11000001', '11000010', '11000011', '11000100', '11000101', '11000110', '11000111', '11001000', '11001001', '11001010', '11001011', '11001100', '11001101', '11001110', '11001111', '11010000', '11010001', '11010010', '11010011', '11010100', '11010101', '11010110', '11010111', '11011000', '11011001', '11011010', '11011011', '11011100', '11011101', '11011110', '11011111', '11100000', '11100001', '11100010', '11100011', '11100100', '11100101', '11100110', '11100111', '11101000', '11101001', '11101010', '11101011', '11101100', '11101101', '11101110', '11101111', '11110000', '11110001', '11110010', '11110011', '11110100', '11110101', '11110110', '11110111', '11111000', '11111001', '11111010', '11111011', '11111100', '11111101', '11111110', '11111111']

good_words = []
for word in words:
    ar = tuple(int(i) for i in word)
    r = MiahNum.Matrix(8,1,*ar)
    dot = T.H*r
    dot = dot.array
    dot = tuple(i%2 for i in dot)
    if dot == (0,0,0,0):
        good_words.append(word)

#print(good_words)
def do():
    new = rd.choices(words,k=3)
    print(*new)
    print("Soft Decoding:")
    print(T.sdecode(*new,loops=50))
    print("Hard Decoding:")
    print(T.hdecode(*new,loops=50))

inp = input('Press enter to run:')
while inp == '':
    do()
    inp = input('>>>')






