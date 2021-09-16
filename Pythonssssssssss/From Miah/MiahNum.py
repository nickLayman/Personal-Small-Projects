e = 2.7182818284590452353602874713527
pi = 3.1415926535897932384626433832795

def ciel(x):
    "Returns ceiling of a real number x"
    return int(x) if int(x) == x else int(x)+1

def floor(x):
    "Returns floor of a real number x"
    return int(x)

def fact(n):
    "Returns n! for non-negative integer n"
    return 1 if n == 0 else n*fact(n-1)

def perm(n,r):
    """Returns nPr for non-negative integers
    n and r, where n>=r"""
    return fact(n)/fact(n-r)

def choose(n,r):
    """Returns nCrfor non-negative integers n
    and r, where n>=r"""
    return perm(n,r)/fact(r)

def lcm(n,m):
    """Returns the lowest common multiple of
    non-negative integers n and m"""
    return min([m*(j+1) for j in range(n) if m*(j+1) in [n*(j+1) for j in range(m)]])

def gcd(n,m):
    """Returns the greates common factor of
    integers n and m"""
    return max(n,m) if 0 in {n,m,n-m} else gcd(min(abs(n),abs(m)),max(abs(n),abs(m))%min(abs(n),abs(m)))

def isPrime(n):
    "Returns True if n is prime, else False"
    return True if pfactor(n) == [n] else False

def isCoprime(m,n):
    """Returns True if n is coprime with m,
    else False"""
    return True if gcd(n,m) == 1 else False

def prod(seq):
    "Returns the product of seq"
    return seq[0]*seq[1] if len(seq)==2 else seq[0]*prod(seq[1:]) if len(seq) > 2 else seq[0] if len(seq)==1 else 1

def sqrt(x):
    "Returns the square root of x"
    return x**(0.5)

def pfactor(n):
    """Returns prime factorization as a list
    with repeats such that
    prod(pfactor(n))=n  ... theoretically"""
    p = [] if n == 1 else [n]
    for i in range(2,ciel(sqrt(n))+1):
        if n%i == 0:
            return [i]+pfactor(int(n/i))
    return p

def factors(n):
    """Returns all factors of an integer n
    as a sorted list"""
    return sorted({i for i in range(1,ciel(sqrt(n))+1) if n%i == 0}.union({n//i for i in range(1,ciel(sqrt(n))+1) if n%i == 0}))

def isPerfect(n):
    """Returns true if an integer n is
    perfect, else false"""
    return True if sum(factors(n))==2*n else False    

def isAbundant(n):
    """Returns true if an integer n is
    abundant, else false"""
    return True if sum(factors(n))>2*n else False    

def isDeficient(n):
    """Returns true if an integer n is
    deficient, else false"""
    return True if sum(factors(n))<2*n else False    

def isPerf(n):
    """Returns Perfect if n is perfect,
    Abundant if n is abundant, or
    Deficient if n is deficient"""
    return "Abundant" if isAbundant(n) else "Perfect" if isPerfect(n) else "Deficient"

def isPower2(x):
    """Returns true if x=2^n for some int n
    else false"""
    x = abs(x)
    while 0 < x < 1.0:
        x = 2*x
    while x > 1.0:
        if x%2 != 0.0:
            return False
        x = x/2
    return True

def scinot(x):
    """Returns x as a tuple (A,n)
    where x=A*10^n"""
    A,n = x,0
    while A >= 10:
        A /= 10
        n += 1
    while A < 1:
        A *= 10
        n -= 1
    return (A,n)
    
def log(x,base=10):
    "Returns log base [base] of x"
    return ln(x)/ln(base)

def ln(x):
    """Returns natural log of x
    accurate to about 14 decimal places"""
    if x <= 0:
        raise ValueError("No log for x<=0") 
    elif x == 1:
        return 0
    elif x>10:
        A,n = scinot(x)
        return n*2.302585092994046+ln(A)
    elif x>1:
        a = max((x+1)/2,1)
        return ln(a)-sum([((1-x/a)**i)/i for i in range(1,1000)])
    else:
        return -ln(1/x)

##arcsin, arccos, arctan,
##arccsc, arcsec, arccot,
##archsin, archcos, archtan,
##archcsc, archsec, archcot
def sin(x):
    "Returns sin(x) for a real number x in radians"
    x = x%(2*pi)
    return sum(((-1)**i)*(x**(2*i+1))/fact(2*i+1) for i in range(0,20))
def cos(x):
    "Returns cos(x) for a real number x in radians"
    x = x%(2*pi)
    return sum((-1)**i*x**(2*i)/fact(2*i) for i in range(0,20))
def tan(x):
    "Returns tan(x) for a real number x in radians"
    x = x%pi
    return inf() if cos(x) == 0 else sin(x)/cos(x)
def csc(x):
    "Returns csc(x) for a real number x in radians"
    return inf() if sin(x) == 0 else 1/sin(x)
def sec(x):
    "Returns sec(x) for a real number x in radians"
    return inf() if cos(x) == 0 else 1/cos(x)
def cot(x):
    "Returns cot(x) for a real number x in radians"
    return inf() if sin(x) == 0 else cos(x)/sin(x)
def sinh(x):
    "Returns sinh(x) for a real number x"
    return 0.5(e**x-e**(-x))
def cosh(x):
    "Returns cosh(x) for a real number x"
    return 0.5(e**x+e**(-x))
def tanh(x):
    "Returns tanh(x) for a real number x"
    return inf() if cosh(x) == 0 else sinh(x)/cosh(x)
def csch(x):
    "Returns csch(x) for a real number x"
    return inf() if sinh(x) == 0 else 1/sinh(x)
def sech(x):
    "Returns sech(x) for a real number x"
    return inf() if cosh(x) == 0 else 1/cosh(x)
def coth(x):
    "Returns coth(x) for a real number x"
    return inf() if sinh(x) == 0 else cosh(x)/sinh(x)
def arcsin(x):
    "Returns arcsin(x) in radians for a real number x Doesn't work rn "
    return -arcsin(-x) if x<0 else pi/2 if x == 1 else sum(
        (x**(2*n+1))*prod(list(
            (2*i-1)**2 for i in range(2,n))
                          )/fact(2*n+1) for n in range(85))
def test():
    import math
    for i in range(-10,11):
        print(i/10, arcsin(i/10)-math.asin(i/10))
        
#test()

class Polynom:
    """Creates a polynomial object with args
    as the coefficients and term degree in
    ascending order """
    def __init__(self,*args):
        self.args = args if args != () else (0,) 
        self.func = lambda x: sum(j*(x**i) for i,j in enumerate(args))
        self.degree = len(args)-1
    def __add__(self, polynom):
        if type(polynom) == Polynom:
            arg1,arg2 = len(self.args),len(polynom.args)
            if arg1 != arg2:
                self.args += (0,)*(max(arg1,arg2)-min(arg1,arg2))
                polynom.args += (0,)*(max(arg1,arg2)-min(arg1,arg2))
            args = (i+j for i,j in zip(self.args,polynom.args))
        elif type(polynom) in {int, float}:
            args = (self.args[0]+polynom,)+self.args[1:]
        return Polynom(*args)
    def __sub__(self, polynom):
        if type(polynom) == Polynom:
            arg1,arg2 = len(self.args),len(polynom.args)
            if arg1 != arg2:
                self.args += (0,)*(max(arg1,arg2)-min(arg1,arg2))
                polynom.args += (0,)*(max(arg1,arg2)-min(arg1,arg2))
            args = (i-j for i,j in zip(self.args,polynom.args))
        elif type(polynom) in {int, float}:
            args = (self.args[0]-polynom,)+self.args[1:]
        return Polynom(*args)
    def __mul__(self,polynom):
        if type(polynom) == Polynom:
            new_arg = tuple()
            for i,j in enumerate(self.args):
                #the 0 tuple ensures proper degree, the j*k ensures proper coefficients
                arg = tuple(0 for k in range(i))+tuple(j*k for k in polynom.args)
                new_arg = Polynom._tup_add(arg,new_arg)
        elif type(polynom) in {int, float}:
            new_arg = tuple(polynom*i for i in self.args)
        return Polynom(*new_arg)
    def __pow__(self, n):
        return prod(list(self for i in range(n))) if n > 0 else Polynom(1) 
    def __floordiv__(self,polynom):
        if type(polynom) == Polynom:
            arg1 = Polynom._tup_strip(self.args)
            arg2 = Polynom._tup_strip(polynom.args)
            lst = [0]*(self.degree-polynom.degree+1)
            i = -1
            while len(arg1) >= len(arg2):
                i += 1
                c = arg1[-1]/arg2[-1]
                lst[i] = c
                arg1 = Polynom._tup_add(arg1,tuple(0 for i in range(len(arg1)-len(arg2)))+tuple(-c*i for i in arg2))
                arg1 = Polynom._tup_strip(arg1)
            lst.reverse()
            tup = tuple(lst)
        elif type(polynom) in {int, float}:
            tup = tuple(i/polynom for i in self.args)
        return Polynom(*tup)
    def __truediv__(self,polynom):
        ########################
        ## do this eventually ##
        ########################
        if type(polynom) == Polynom:
            pass
        elif type(polynom) in {int, float}:
            tup = tuple(i/polynom for i in self.args)
            return Polynom(*tup)
    def __mod__(self,polynom):
        p = self-((self//polynom)*polynom)
        return Polynom(*(Polynom._tup_strip(p.args)))
    def __str__(self):
        try:
            s = "{}+{}x".format(self.args[0],self.args[1])
            s = s+"".join("+"+str(j)+"x^"+str(i) for i,j in enumerate(self.args[2:],start=2))
        except IndexError:
            try:
                s = "{}+{}x".format(self.args[0],self.args[1])
            except IndexError:
                s = "{}".format(self.args[0])        
        return s
    def __call__(self,arg):
        return self.func(arg)
    def __repr__(self):
        return "Polynom{}".format(self.args)
    def __eq__(self,polynom):
        return True if self.args == polynom.args else False 
    def __lt__(self,polynom):
        return True if self.degree < polynom.degree else False 
    def __le__(self,polynom):
        return True if self.degree <= polynom.degree else False 
    def __ne__(self,polynom):
        return True if self.degree != polynom.degree else False 
    def __ge__(self,polynom):
        return True if self.degree > polynom.degree else False 
    def __gt__(self,polynom):
        return True if self.degree >= polynom.degree else False
    def __or__(self,polynom):
        ## use to find intersection of two polynoms
        pass
    @classmethod
    def zero(cls):
        return cls(0)
    @staticmethod
    def _tup_add(tup1, tup2):
        arg1 = len(tup1)
        arg2 = len(tup2)
        if arg1 != arg2:
            tup1 += (0,)*(max(arg1,arg2)-min(arg1,arg2))
            tup2 += (0,)*(max(arg1,arg2)-min(arg1,arg2))
        args = tuple(i+j for i,j in zip(tup1,tup2))
        return args
    def _tup_strip(tup):
        try:
            while tup[-1]==0:
                tup = tup[:-1]
        except:
            pass
        finally:
            return tup

class Rational:
    def __init__(num,denom):
        pass
    def __add__(self, polynom):
        pass
    def __sub__(self, polynom):
        pass
    def __mul__(self,polynom):
        pass
    def __pow__(self, n):
        pass
    def __floordiv__(self,polynom):
        pass
    def __truediv__(self,polynom):
        pass
    def __mod__(self,polynom):
        pass
    def __str__(self):
        pass
    def __call__(self,arg):
        pass
    def __repr__(self):
        pass
    def __eq__(self,polynom):
        pass
    def __lt__(self,polynom):
        pass
    def __le__(self,polynom):
        pass
    def __ne__(self,polynom):
        pass
    def __ge__(self,polynom):
        pass
    def __gt__(self,polynom):
        pass
    
class Matrix:
    def __init__(self,n,m,*array):
        self.array = array
        self.m = m
        self.n = n
        if len(array) < m*n:
            array+(0,)*(m*n-len(array))
        array = list(array)
        self.mat = []
        for i in range(n):
            self.mat.append(list([array.pop(0) for i in range(m)]))
    def __str__(self):
        return "".join(str(i)+"\n" for i in self.mat)
    def __repr__(self):
        return "".join(str(i)+"\n" for i in self.mat)
    def __add__(self, other):
        if (self.m,self.n)!=(other.m,other.n):
            raise ArithmeticError("Matrices must have the same size to add them")
        new = tuple(self.array[i]+other.array[i] for i in range(self.m*self.n)) 
        return Matrix(self.n,self.m,*new)    
    def __sub__(self,other):
        if (self.m,self.n)!=(other.m,other.n):
            raise ArithmeticError("Matrices must have the same size to subtract them")
        new = tuple(self.array[i]-other.array[i] for i in range(self.m*self.n)) 
        return Matrix(self.n,self.m,*new)    
    def __mul__(self,other):
        if self.m!=other.n:
            raise ArithmeticError("Matrices not compatible for multiplication")
        new = []
        for i,j in [(i,j) for i in range(self.n) for j in range(other.m)]:
            new.append(sum(self.mat[i][k]*other.mat[k][j] for k in range(self.m)))
        return Matrix(self.n,other.m,*new)
    def __pow__(self, n):
        return prod(self for i in range(n))
    def __eq__(self,other):
        return True if self.mat==other.mat else False
    def __ne__(self,other):
        return True if self.mat!=other.mat else False
    def ind(self,i,j):
        return self.mat[i][j]
    def inv(self):
        "Returns inverse matrix"
        pass
    def trans(self):
        "Returns transpose matrix"
        pass
    def ref(self):
        "Returns matrix in Roe-Echelon form"
        pass
    def rref(self):
        "Returns matrix in reduces Roe-Echelon form"
        pass

    @classmethod
    def zero(cls,n,m):
        return cls(n,m,*(0 for i in range(n*m)))
    @classmethod
    def I(cls,n):
        array = ()
        for i,j in [(i,j) for i in range(n) for j in range(n)]:
            array += (0,) if i!=j else (1,)
        return cls(n,n,*array)

class Vector:
    pass

class inf:
    def __str__(self):
        return 'inf'
    def __repr__(self):
        return 'inf'






    
