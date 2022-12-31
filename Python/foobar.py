# a cellular automaton is described where
# in a boolean array with 3-9 rows and 3-50 columns
# and at each time step the cell (i, j) is transformed
# according to the rules:
# if exactly one of (i, j), (i+1, j), (i, j+1), and (i+1, j+1)
# are True, then (i, j) will be True in the next time step.
# otherwise (i, j) will be False in the next time step.
# if one of those 4 do not exist, (i, j) will not exist in the next time step
# so the grid loses the bottom row and right-most column at each time step

# given the result of this automaton,
# write an inverse function to determine how many
# states would result in the provided grid.

# How many unique grid states would result in grid G after 1 time step?



# Given examples:
# -- Python cases --
# Input:
# solution.solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
# Output:
#     11567

# Input:
# solution.solution([[True, False, True], [False, True, False], [True, False, True]])
# Output:
#     4

# Input:
# solution.solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
# Output:
#     254



# first thought: figure out the small cases and try to combine them for large ones
# [False] has 1+4+4+1=10 previous states, depending on the number of Trues
# [True] has 4 previous states, anything with just 1 True
# [False, False] has 2+1+4+3+3+3+3+4+4=27 previous states
# [True, False] has 2*2 + 2*3 = 10 depending on if the True came from a 
#               True in the first or second column previously
#

# maybe using binary for True and false would reveal something
# or at least make it easier to write and think about

# working left to right means cases for each possibility on the left
# and following each case through to the right to count possibilities
# maybe working right to left would be easier since adding
# a left column would not affect the viability of the right columns
# similarly, maybe working from the bottom is best

# which conclusion states are impossible?

# Could assign each 2x2 matrix a number/label 0-15
# and figure out all possible label pairs
# for two horizontal or vertical or diagonal
# cells. 
# Going to each cell would have a running count
# of valid choices. Maybe a set of pairs with
# a valid label and a multiplier for how many times it could be valid

# run from bottom right, then left, then up a row
# so that each cell can be calculated only
# from previously calculated ones

# for each cell in that order
# have a list of pairs (label, possible?)
# for each label, if that configuration could apply, 
# given the nearby 3 cells, let possible=True

# then run through all the cells and take the
# product of how many Trues there are in each list

# the label is unnecessary, we can just use the index

# maybe figure out all True False 2x2 grids
# and how many 3x3 grids could make each one
# then go through the 2x2 grids 

# labeling the 2x2 will just be the binary
# reading normally so [[0, 1], [1, 0]] is labelled/index 6

# what horizontal pairs workfor [True, True], etc.
# making a function to do this for me is probably better
# maybe generate all 2x3 boolean arrays, figure out their pair, 
# and figure out the resulting 1x2 array
# or do all 3x3 and work out each pair


# horiz_bool_pair_to_labels = {pair:set() for pair in [
#                             (False, False), 
#                             (False, True), 
#                             (True, False), 
#                             (True, True)]}
# vert_bool_pair_to_labels = {pair:set() for pair in [
#                             (False, False), 
#                             (False, True), 
#                             (True, False), 
#                             (True, True)]}
# maj_diag_bool_pair_to_labels = {pair:set() for pair in [
#                             (False, False), 
#                             (False, True), 
#                             (True, False), 
#                             (True, True)]}
# min_diag_bool_pair_to_labels = {pair:set() for pair in [
#                             (False, False), 
#                             (False, True), 
#                             (True, False), 
#                             (True, True)]}

# horizontal_label_pair = {label:set() for label in range(16)}
# vertical_label_pair = {label:set() for label in range(16)}
# diagonal_label_pair = {label:set() for label in range(16)}

# label_to_mat = {}
# mat_to_label = {}
label_to_col = {}
col_to_label = {}


def gen_col_labels(height):
    global label_to_col
    global col_to_label

    label_to_col = {}
    col_to_label = {}

    format_str = '0' + str(height) + 'b'
    for label in range(2**height):
        b_str = format(label, format_str)
        col = tuple(bool(int(char)) for char in b_str)
        label_to_col[label] = col
        col_to_label[col] = label


def get_col_pair_image(col_pair):
    image_col = []
    for idx, row in enumerate(col_pair[:-1]):
        row_2 = col_pair[idx+1]
        image_col.append(sum(row)+sum(row_2) == 1)
    return image_col


def get_col_preimages(image_col, first_columns=None):
    global label_to_col
    global col_to_label
    
    if first_columns == None:
        first_columns = label_to_col
    else:
        first_columns = {label:label_to_col[label] for label in first_columns}
    preimages = []
    for label_1, col_1 in first_columns.items():
        skip = False
        for idx, row in enumerate(image_col):
            if row and col_1[idx]+col_1[idx+1]==2:
                skip = True
        if skip:
            continue
        for label_2, col_2 in label_to_col.items():
            col_pair = [[pair[0], pair[1]] for pair in zip(col_1, col_2)]
            if get_col_pair_image(col_pair) == image_col:
                preimages.append((label_1, label_2))
    return preimages


def solution(g):
    global label_to_col
    global col_to_label
    preimage_height = len(g)+1
    
    gen_col_labels(preimage_height)

    image_col = [row[0] for row in g]
    edges_12 = get_col_preimages(image_col)
    col_1_counts = {}
    col_2_counts = {}
    for pair in edges_12:
        col_1_counts[pair[0]] = 1
        col_2_counts[pair[1]] = 0

    for col_idx in range(1, len(g[0])):
        image_col = [row[col_idx] for row in g]
        edges_23 = get_col_preimages(image_col, first_columns=col_2_counts.keys())
        col_2_counts = {}
        col_3_counts = {}
        for pair in edges_23:
            col_2_counts[pair[0]] = 0
            col_3_counts[pair[1]] = 0

        for pair in edges_12:
            if pair[1] in col_2_counts.keys():
                col_2_counts[pair[1]] += col_1_counts[pair[0]]

        edges_12, edges_23 = edges_23, None
        col_1_counts, col_2_counts, col_3_counts = col_2_counts, col_3_counts, None

    for pair in edges_12:
        col_2_counts[pair[1]] += col_1_counts[pair[0]]

    final_sum = 0
    for key, val in col_2_counts.items():
        final_sum += val

    return final_sum


# answer 11567
print(solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]))

# answer 4
print(solution([[True, False, True], [False, True, False], [True, False, True]]))

# answer 254
print(solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]))






# def fill_dicts():
#     for label1, mat1 in label_to_mat.items():
#         bool1 = sum(mat1[0])+sum(mat1[1])==1
#         bool_label_to_mats[bool1].add(mat1)

#         for label2, mat2 in label_to_mat.items():
#             bool2 = sum(mat1[0])+sum(mat1[1])==1



# after all that started feeling too complicated
# and interconnected, 
# let's try making this an integer programming problem
# or a system of equations. 
# Each True gives us an equation
# where the sum of 4 binary variables is 1.
# maybe we only need to focus on the cells 
# that are True and filling in the rest is easy to count?

# 

























# # # need to calculate sum(floor(i*sqrt(2)), i, 1, n) for very large n

# # # I think all I need to know
# # # is at which multiples of sqrt(2)
# # # it passes one or two integers.
# # #
# # # the summand always goes up by at 
# # # least 1 but sometimes 2

# # # I feel like this could be
# # # done with egyptian fractions.
# # # egyptian fractions would be good
# # # for getting many but not all of these
# # # floor values. the issue arises when
# # # the fractions add together like
# # # 2/3 + 6/13 > 1
# # # this is when the summand jumps by 2

# # # if we assume sqrt(2) is rational and = a/b
# # # then we are summing floor(a*i/b) for i from 1 to n
# # # which takes the integer part of a*i/b
# # # with the division algorithm we can write
# # # a*i = q*b + r with the usual restrictions
# # # for all i we are summing up the corresponding q value
# # # if we instead write a = q*b + r we know q=1
# # # then a*i = (q*i)*b + r*i = i*b + r*i
# # # and a*(i+1) = (i+1)*b + r*(i+1) = (i+1)*b + r*i + r
# # # if r*(i+1) >= b then a*(i+1) = (i+2)*b + r*(i+1)-b
# # # all of the issues come from finding out when
# # # multiples of r add to more than b.
# # # the rollover occurs at all i where r*i >= b
# # # so where i >= b/r.
# # # 
# # # so starting with i=1 and increasing we have
# # # a*1 = 1*b + r, add i=1 to the sum
# # # and for all i < b/r we will add i to our sum.
# # # 
# # # at the first i > b/r:
# # # a*i = i*b + i*r and i*r >= b 


# # # other thought: get sqrt(2) very precisely

# # # using Decimal offers arbitrary precision in finding sqrt(2)

# # # good under-approximations a/b for sqrt(2) mean that 
# # # sqrt(2) - a/b > 0 but small so sqrt(2) - a/b = epsilon so
# # # b*sqrt(2)  = a + b*epsilon
# # # i*b*sqrt(2) = i*a + i*b*epsilon
# # # so multiples of b*sqrt(2) will round down to multiples of a
# # # this lets us sum arithmetic sequences of our sum
# # # but works better for larger a and b
# # # and works badly for, say, b=1. 
# # # the length of the sequence also depends on
# # # how good of an approximation a/b is compared
# # # to how big b is. we need "efficient", low-denominator approximations

# # # every term is floor(i*sqrt(2))
# # # taking the floor is rounding down to 
# # # the previous integer but is also just subtracting
# # # a bit off. 
# # # floor(i*sqrt(2)) = i*sqrt(2) - 


# # import math
# # import fractions
# # import decimal

# # decimal.getcontext().prec=200


# # def greedy_egyptian_float(x):
# #     denominators = [math.floor(x)]
# #     x -= math.floor(x)

# #     for i in range(25):
# #         if x > 0:
# #             denominators.append(math.ceil(1./x))
# #             x -= 1./denominators[-1]
# #     return denominators


# # def greedy_egyptian_frac(a, b):
# #     if a > 0:
# #         divisor = fractions.gcd(a, b)
# #         a /= divisor
# #         b /= divisor
# #     denominators = [a/b]
# #     a -= b*denominators[-1]

# #     for i in range(25):
# #         if a > 0:
# #             divisor = fractions.gcd(a, b)
# #             a /= divisor
# #             b /= divisor
# #             if b%a == 0:
# #                 denominators.append(b/a)
# #             else:
# #                 denominators.append(b/a+1)
# #             a = a*denominators[-1] - b
# #             b = b*denominators[-1]
# #     return denominators


# # def continued_frac(x):
# #     denominators = [math.floor(x)]
# #     x -= denominators[0]

# #     for i in range(25):
# #         if x > 0:
# #             x = 1/x
# #             denominators.append(math.floor(x))
# #             x -= denominators[-1]
# #     return denominators


# # def solution(s):
# #     # Your code here
# #     egyptian_denominators = [1, 3, 13, 253, 218201, 61323543802, 5704059172637470075854, 178059816815203395552917056787722451335939040, 227569456678536847041583520060628448125647436561262746582115170178319521793841532532509636]
# #     n = long(s)

# # egyptian_denominators = [1, 3, 13, 253, 218201, 61323543802, 5704059172637470075854, 178059816815203395552917056787722451335939040, 227569456678536847041583520060628448125647436561262746582115170178319521793841532532509636]


# # # a, b = 2L, 1L
# # # for i in range(75):
# # #     a, b = b, a 
# # #     a += 2*b
# # #     # print(a, b, float(a)/b)
# # # a -= b

# # # print(greedy_egyptian_float(math.sqrt(2)))
# # # denoms = greedy_egyptian_frac(a, b)
# # # # print(denoms)
# # # val = denoms[0]
# # # print(0, val)
# # # for i, denom in enumerate(denoms[1:10]):
# # #     val += 1./denom
# # #     print(i+1, val, denom)

# # # print(a, b, float(a)/b)

# # # for i in range(1, 40):
# #     # print(b*i*decimal.Decimal(2).sqrt() - a*i)

# # root_2_dec = decimal.Decimal(2).sqrt()
# # # root_2_frac = fractions.Fraction(root_2_dec)

# # # partial_sum_frac = fractions.Fraction(0, 1)
# # # for den in egyptian_denominators[:6]:
# # #     partial_sum_frac += fractions.Fraction(1, den)
# # # print(partial_sum_frac)

# # # for i in range(1, 20):
# # #     print(partial_sum_frac.denominator*i*root_2_dec - partial_sum_frac.numerator*i)

# # # print(decimal.Decimal(partial_sum_frac.numerator)/decimal.Decimal(partial_sum_frac.denominator) - root_2_dec)

# # # true_sum = 0
# # # floor_sum = 0
# # # error_sum = 0
# # # for i in range(1, 20001):
    
# # #     floor_val = int(math.floor(i*root_2_dec))
    
# # #     floor_sum += floor_val

# # #     if i%1001 == 0:
# # #         true_val = i*root_2_dec
# # #         error_val = true_val - floor_val

# # #         true_sum = decimal.Decimal(i*(i+1))/root_2_dec
# # #         error_sum = true_sum - floor_sum

# # #         print(i)
# # #         print("\t" + str((round(true_val, 3), round(floor_val, 3), round(error_val, 3))))
# # #         print("\t" + str((round(true_sum, 3), round(floor_sum, 3), round(error_sum, 3))))
# # #         print("\t" + str(round(error_sum/i, 5)))
# # #         print("\t" + str(round(error_sum - decimal.Decimal(i)/decimal.Decimal(2), 3)))
# # #         print("\t" + str(round((math.ceil(true_sum) - math.ceil(decimal.Decimal(i)/decimal.Decimal(2))) - floor_sum, 3)))



# # # trying out a formula found online
# # def brute_force(n):
# #     val = long(0)
# #     for i in range(n+1):
# #         val += long(i*root_2_dec)
# #     return val


# # def beni(n):
# #     if n == 1:
# #         return 1 
# #     if n == 0:
# #         return 0
# #     r = decimal.Decimal(2).sqrt()
# #     N = long(n*r)
# #     s = decimal.Decimal(1)/decimal.Decimal(r)
# #     s = decimal.Decimal(1) - s
# #     s = decimal.Decimal(1)/s
# #     k = long(decimal.Decimal(N)/s)
# #     val = N*(N+1)/2 - k*(k+1) - beni(k)
# #     return val


# # for i in range(1, long(1e100), long(1e99+1)):
# #     print(beni(i))




# import decimal
# decimal.getcontext().prec=200

# def solution(s):
#     # Your code here
#     n = long(s)
#     if n == 1:
#         return 1 
#     if n == 0:
#         return 0
#     r = decimal.Decimal(2).sqrt()
#     N = long(n*r)
#     s = r+2
#     k = long(decimal.Decimal(N)/s)
#     val = N*(N+1)/2 - k*(k+1) - long(solution(str(k)))
#     return str(val)


# # after a lot of deadends thinking about
# # egyptian fractions, continued fractions,
# # modular arithmetic, approximating sqrt(2)
# # with rationals, and other cool math,
# # I came across Beatty sequences, 
# # essentially exactly what we're summing here
# # The website I found on them for summing floor(phi): 
# # https://mathproblems123.wordpress.com/2020/07/25/sum-of-floors-of-multiples-of-the-golden-ratio/

# # the sequence made with floor(i*s) for natural
# # numbers i for some irrational s>1

# # each Beatty sequence for some s>1 has 
# # a complementary Beatty sequence, the one
# # for r>1 where 1/s + 1/r = 1

# # it's known that complementary Beatty sequences
# # are disjoint yet cover the natural numbers.

# # using that, and the fact that the complementary
# # sequence for sqrt(2) is the sequence for sqrt(2)+2, 
# # I found and simplified a recursive sequence
# # giving the above function.

# # essentially, for certain summation indices we have
# # sum(floor(i*sqrt(2))) + sum(floor(i*(sqrt(2)+2))) = sum(i)
# # since they must cover up to some integer

# # the max index in the first sum is our given s, 
# # the max index on the right sum is the max int found
# # in the sequence we're observing, i.e. floor(n*s)
# # the remaining max index is the index giving the
# # largest multiple of (sqrt(2)+2) less than floor(n*s)

# # from there we can expand i*(sqrt(2)+2) to give
# # 2*i + i*sqrt(2), and since 2*i is an integer
# # being added, we can remove it from the floor
# # and consider it's sum separately. 

# # so we have 
# # sum(floor(i*sqrt(2))) + sum(2*i) + sum(floor(i*sqrt(2))) = sum(i)
# # with differing maximum indices
# #
# # getting sum(i) and sum(2*i) is easy
# # and the differing index on the other sum(floor(i*sqrt(2)))
# # is what gives us our recursion

# # the maximum index being calculated decreases
# # by a factor of approximately sqrt(2)/(sqrt(2)+2) every step
# # which is (sqrt(2) - 1) and about 0.414
# # so the scale of the calculation significantly decreases at each step
# # and this is O(log(n))


# # answer 19
# print(solution('5'))
# # answer 4208
# print(solution('77'))



















# level 5 completed, received an encrypted message
# used code found online to decrypt it

# import base64
# from itertool import cycle
#
# message = "FU4QHg8CHB4SSRkDTk4EGQkADUpNTh5aAQUPDg0GDAhGTgMZSQwQHwkEFAgFSRUZSQwFDQMTDR5G TgMZSQANCB4EHQQDAlweQklECg8JEAgXC1RcAB1ES1ZBXhgPAlZaBQwHTEBBXh8ADFtQGhpES1ZB Xh4ACFweQklEDQMOXk1bTh5OBwdCTBE="
#
# key = bytes("nicklayman99", "utf8")
# print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
#
# printed the message: 
# b"{'success' : 'great', 
# 'colleague' : 'esteemed', 
# 'efforts' : 'incredible', 
# 'achievement' : 'unlocked', 
# 'rabbits' : 'safe', 
# 'foo' : 'win!'}"










# # first thought for an overall process:
#     # find an easy way to check if two grids are equivalent.
#     # then maybe we can brute force it.
# # a mental connection:
#     # equivalence and permutations are really pushing
#     # me mentally towards some group theory but even so, 
#     # I want an easy equivalence check first. 
# # first thought for checking equivalence:
#     # row swaps and column swaps do not change row multisets
#     # or column multisets.
#     # does having the same row multisets and column multisets
#     # imply equivalence?
#     # no, I found a counterexample
#     # 1 0 1         1 1 0
#     # 2 1 0   and   2 0 1
#     # 3 2 1         3 2 1
#     # same row and col multisets but no way to go between
#     # them with just row and column swaps
# # note on equivalence:
#     # there's a bit of work to fully show this 
#     # but I did that work. if given a grid, 
#     # to obtain any other grid in its equivalence class,
#     # you never need more than one permutation of rows and
#     # one permutation of columns and the order of these
#     # permutations doesn't matter.
# # note on computability:
#     # permuting the rows of a matrix A can be done by
#     # multipyling by a permutation matrix P_r like P_r*A
#     # similarly, permuting columns needs a permutation
#     # matrix P_c and multiplying like A*P_c
#     # so the equivalence class of some grid G is all
#     # matrices of the form P_r*G*P_c
# # a mental connection:
#     # matrices of that form is making me think
#     # of "similar" matrices but similar matrices
#     # is a stricter form than we have. It needs
#     # a matrix and it's inverse on the two sides
# # computability:
#     # checking equivalence between A and B
#     # is equivalent to finding permutations P_r and P_c
#     # such that A*P_c = P_r^{-1}*B
#     # a permutation's inverse is a permutation so
#     # that can also be written as A*P_c = P_r*B
#     # so we can permute just columns of A and just rows of B.
#     # so maybe we use the rows of B as a template to force
#     # column permutations in A. it feels like this would
#     # keep the number of permutations down a lot
# # mental connection:
#     # from group theory, the form g*a*g^{-1} is conjugation
#     # but here we have possibly different elements on the 
#     # left and right so it's not the same idea.
# # computability:
#     # permutation matrices are orthogonal
#     # so their inverse is their transpose
# # mental connection:
#     # the set of matrices we're working on is
#     # X = M_{m x n}([k]) where [k] = {0, 1, ..., k-1};
#     # i.e., the m x n matrices with symbols from [k]
#     # ([k] is defined this way to have exactly k symbols).
#     # permuting rows of a set of matrices is a 
#     # group action; the permutation group S_m acting on 
#     # that set of matrices. similarly for columns.
#     # 
#     # focusing just on row permutations,
#     # the permutation group S_m takes each matrix A
#     # and maps it to some other matrices by swapping 
#     # the rows of A. this is a left group action and
#     # puts each matrix into an orbit
#     # and those orbits are our equivalence classes, X/S_m, 
#     # the quotient of the action.
#     # this action is faithful, not transitive, 
#     # and not (fixed-point) free.
#     # the stabilizer subgroup for each matrix should be
#     # easy to find and count by counting identical rows.
#     # but this requires generating every matrix and finding
#     # its identical rows. counting identical rows is easy
#     # for matrices with width and height < 12 but the
#     # matrix generation alone (with brute force)
#     # would take far too long.
#     # 
#     # we could easily figure out how many unique rows are 
#     # possible (k^width) and count all matrices with, say,
#     # exactly 2 identical rows at the same time without
#     # generating any. but counting all matrices with some
#     # collection of numbers of identical rows without generation
#     # would not always be straightforward. In most cases
#     # it may come down to integer partitions but not all
#     # partitions are possible. For example, in a height 3 
#     # width 1 matrix with 2 symbols, it is impossible to 
#     # have all unique rows. similarly for any matrix where 
#     # (height, width, num symbols) = (>x^y, y, x)
#     # including (>2, 1, 2), (>4, 2, 2), (>9, 2, 3), (>8, 3, 2)
#     # 
#     # counting orbits of this action is what we're after.
#     # we can do this with burnsides lemma: 
#     # |X/S_m| = sum(|X^s|, s in S_m)/|S_m|
#     # where X^s is the set of x fixed by s
#     # counting fixed points of a given permutation seems
#     # easier than counting a matrix's fixing-permutations
#     # since we won't run into the same problem with the
#     # pigeonhole principle as above. if a permutation fixes
#     # matrix A, it doesn't matter that other rows could also
#     # be permuted, just that this permutation fixes it. 
#     # 
#     # I think doing row and column permutations at the same time
#     # could be equivalent to the direct product of 
#     # the permutation groups acting on X by permuting the 
#     # rows and columns as defined by each permutation.
#     # so S_m x S_n acting on X in the way we expect. 
#     # 
#     # though online I just found a direct product action
#     # setup to where it would be S_m x S_n acting on X
#     # by (s_m, s_n)A = s_m * A * s_n^{-1}
#     # this is so that the action axioms are satisfied.
#     # this action could be useful to remember
#     # and wouldn't change our counting since the inverse 
#     # of a column perm is a column perm that we would've 
#     # done anyway. plus, the fixed points of s_n are exactly
#     # the fixed points of s_n^{-1} so the count won't change
    
# # math:
#     # for each permutation, how many matrices are fixed?
#     # identity: all s^(w*h) 
#     # a particular transposition: s^(w*(h-1))
#     # there are (h choose 2) row transpositions
#     # two disjoint transpositions: s^(w*(h-2))
#     # there are (h choose 2)*(h-2 choose 2) = (h choose 4)*6
#     # pairs of disjoint transpositions
#     # 
#     # for a general permutation: find the sets of rows that 
#     # must be identical by finding the permutation's cycles
#     # (or at least knowing cycle lengths), 
#     # then count how many ways we can construct 1 row from
#     # each set/cycle, and the remaining rows are determined.
#     # 
#     # so instead of counting with transpositions, we 
#     # count with cycle lengths, which we can use integer
#     # partitions for. 
#     # every integer partition of the number of rows has
#     # at least one corresponding row permutation where the
#     # cycle lengths are the integers in the partition.
#     # the (sorted) partition is the permutation's cycle type. 
#     # 
#     # the counting per row permutation is then easy; 
#     # when we are ignoring some number of rows (because
#     # they are determined), it's equivalent to counting 
#     # the total number of shorter matrices. Like with 
#     # the transpositions count above, it's just counting 
#     # w x (h-1) matrices with s symbols.
#     # 
#     # similarly, counting a column permutation's fixed points
#     # is equivalent to counting thinner matrices.

# # how to combine row and column permutations?
#     # as stated above, for each row permutation we construct
#     # 1 row per cycle and consider the rest determined.
#     # a particular pair of row and column permutations
#     # lets us construct those same rows without restriction
#     # except for the row elements in the column permutation's
#     # cycles which rely on / are determined by each other. 
#     # 
#     # The number of intersections between a row and 
#     # each column permutation cycle is the same as the cycle
#     # length and vice versa so that's not an issue (every
#     # row intersects every column exactly once). 
#     # 
#     # instead of ignoring all row elements intersecting
#     # a column cycle of length more than 1 and constructing 
#     # them later (which was my first thought), we can instead
#     # pick exactly 1 element per column cycle in each row.
#     # the remaining row elements intersecting column cycles
#     # are determined since they must be identical to that
#     # cycle's representative in that row. 
#     # since we'd then have the same number of determined
#     # elements in each row, this is equivalent to counting
#     # thinner matrices.

# # constructing a permutation's fixed points:
#     # for each row cycle, construct one row (essentially
#     # constructing a shorter matrix) without restriction 
#     # except only choosing one row element per column cycle
#     # (essentially constructing a thinner matrix).
#     # 
#     # we count fixed rows as being in a cycle of length 1.
#     # so this constructs "most" elements in "most" rows, 
#     # and the remaining row elements in those rows must copy 
#     # some other element in that row determined by the 
#     # column permutation, and the remaining rows must copy 
#     # some previously constructed row. So all matrix elements 
#     # are either chosen explicitly or determined by the cycles.
#     # 
#     # with a fixed permutation, this is equivalent to 
#     # constructing a single, shorter, thinner matrix 
#     # over the same symbol set without any restrictions. 
#     # making the count s^((w - a)*(h - b)) where a and b
#     # are determined by the cycle types of the row permutation
#     # and the column permutation. we only construct one row
#     # per row cycle so the height of this shorter matrix
#     # is equal to the number of row cycles, which would
#     # be equal to the length of the row cycle type list. 
#     # similarly the width would be the length of the column
#     # cycle type list. 
#     # 
#     # in addition to corresponding to integer partitions,
#     # the distinct cycle types of the permutations of S_n also
#     # define the conjugacy classes of S_n. two partitions
#     # are in the same conjugacy class if and only if they
#     # have the same cycle type. and since the cycle types of
#     # each row/column permutation pair for us defines the 
#     # number of fixed points, we need the number of permutations
#     # per cycle type (and thus the size of each conjugacy
#     # class) to use as a multiplier for these terms. 
#     # 
#     # can we use the class equation here at all? the center
#     # of the symmetric group is just the identity. I don't
#     # think we can use it nicely here. but counting the size
#     # of each conjugacy class once we have cycle type is not 
#     # too hard

# # counting satisfactory permutations:
#     # once we know a permutation and its cycle type
#     # we can count its fixed points, contributing one
#     # term to the sum in burnside's lemma

# # key math:
#     # we want the number of equivalence classes
#     # defined by the relation of row and column permutations.
#     # so the number of orbits under the action of the group
#     # that swaps rows and swaps columns. this is S_m x S_n
#     # where S_m permutes rows and S_n permutes columns
#     # for just row permutations:
#         # |X/S_m| = sum(|X^s|, s in S_m)/|S_m|
#         # the number of orbits (equivalence classes) under
#         # just row permutations is equal to
#         # (the sum of the number of fixed points per permutation)
#         # divided by the order of the group (m!)
#     # for both row and column permutations:
#         # |X/(S_m x S_n)| = sum(|X^s|, s in S_m x S_n)/|S_m x S_n|
#         # the number of orbits (equivalence classes) under 
#         # row and column permutations (what we want) is equal to
#         # (the sum of the number of fixed points per permutation)
#         # divided by the order of the group (m!*n!) 
#     # given a permutation:
#         # the permutation's cycle type defines the number
#         # of elements it fixes. Specifically, how many
#         # row cycles r and how many column cycles c it has
#         # determines how many matrices it fixes given by
#         # s^(c*r) 
#     # given a row cycle type:
#         # we'd like to know how many permutations exist
#         # satisfying that row permutation cycle type.
#         # a row cycle type [c_1, c_2, ..., c_t] is satisfied by
#         # the product of the number of ways to make a cycle out
#         # of c_1 rows from r rows, times the number of ways to 
#         # make a cycle out of c_2 rows from r-c_1 rows, etc.
#         # the order of picking rows does matter but not completely.
#         # making a length c_1 cycle from r rows is
#         # (r!)/(c_1*(r-c_1)!) 
#         # note that this is not the choose function, it is
#         # counting permutations of c_1 rows from r total rows
#         # then dividing by c_1 because the start of the cycle
#         # is irrelevant. 
#         # so a row_cycle_type=[c_1, c_2, ..., c_t] is satisfied by
#         # (r!)/(c_1*(r-c_1)!) * ((r-c_1)!)/(c_2*(r-c_1-c_2)!) * ... * ((r-c_1-c_2-...-c_{t-1})!)/(c_t*(r-c_1-...-c_t)!)
#         # permutations.
#         # simplifying:
#         # (r!)/(c_1) * (1)/(c_2) * ... * (1)/(c_t)
#         # = r! / product(row_cycle_type)
#         # to conceptualize the simplification, 
#         # order all rows in one of r! ways, 
#         # the first c_1 make the first cycle, the next c_2
#         # make the second cycle, and so on. 
#         #
#         # but this method will in fact over-count how many
#         # permutations satisfy a cycle type because it does not
#         # take into account the fact that if multiple cycles are the
#         # same length, the order in which those cycles are determined
#         # does not matter, only their elements do.
#         # so the above calculation should be divided by how many
#         # ways the cycle lengths can be inconsequentially rearranged.
#         # so if a cycle length appears 3 times, divide by 3!. if 
#         # another cycle length appears 5 time, further divide by 5!, etc.
#     # column cycle type counts are the same 
#         # just making obvious changes like using the number
#         # of columns and using a valid cycle type for 
#         # a column permutation (a partition of the number of
#         # columns instead of the rows)
#     # given a row and column cycle type:
#         # the number of elements of S_n x S_m satisfying the
#         # cycle types T_n and T_m is simply the product
#         # of the number of permutations satisfying T_n and the 
#         # number of permutations satisfying T_m
#     # given a column and row count (width and height):
#         # with such restricted sizes (up to only 12), 
#         # we can calculate all partitions of the 
#         # width and height relatively easily. 
#         # example: 12 only has 77 partitions.

# # so, outline:
#     # 1) use w and h to generate two lists:
#     # all integer partitions of the column count and
#     # all integer partitions of the row count
#     # 
#     # TODO: have function to obtain all integer partitions
#     # 
#     # these partitions are the cycle types
#     # of column and row permutations respectively.
#     # 
#     # 2) for each (column cycle type, row cycle type) pair,
#     # find how many matrices are fixed by a permutation with
#     # those cycle types. 
#     # 
#     # any two column and row permutation pairs with equal
#     # cycle type lengths, say C column cycles and R row cycles, 
#     # will have the same number of fixed points / matrices
#     # given by s^(C*R). 
#     # 
#     # TODO: have a function to return this count 
#     #       when given cycle types
#     # 
#     # 3) for each (column cycle type, row cycle type) pair,
#     # find how many permutations satisfy that pair 
#     # given by the product of products described above
#     # 
#     # TODO: have a function return this count
#     #       when given cycle types
#     #
#     # 4) for each (column cycle type, row cycle type) pair,
#     # multiply the results of steps 2 and 3 together to obtain
#     # many terms of the burnside's lemma sum at once
#     # 
#     # TODO: have a running sum for burnside's lemma
#     # 
#     # 5) once all terms for burnside's lemma have been summed, 
#     # divide by w!*h! (the order of S_w x S_h) to obtain
#     # the number of orbits of this group action,
#     # i.e. the number of non-equivalent grids. 
#     # 
# #
# #
# # update, I was wrong about one part:
#     # I had mistakenly assumed that if a set of rows
#     # are permuted in a cycle, that all those rows
#     # must be identical even if some columns
#     # are permuted at the same time. one counterexample
#     # to this is the 2x2 identity matrix being fixed
#     # if a row-swap and column-swap happen at the same time.
#     # this changes how to count fixed points.
#     #
#     # previously, where a row cycle and column cycle
#     # intersected, I chose exactly 1 cell from their
#     # intersection and assumed the rest were determined.
#     # my thoughts were equivalent to assuming <1, 1>
#     # could generate Z_n x Z_m for all n, m. 
#     # the <1, 1> comes from us cycling through the rows
#     # and the columns which is equivalent to looking at Z_n
#     # or Z_m. taking one "step" through the permutation
#     # of rows is like adding 1 to the row and similarly for 
#     # the columns. what we need to know is how many
#     # cosets <1, 1> has in Z_n x Z_m which will be 
#     # gcd(n, m). 
#     #
#     # so for every pair of a row cycle and a column cycle,
#     # I get to determine gcd(n, m) cells instead of just 1
#     # 
#     # since we're including cycles of length 1, this can 
#     # just come down to looking at every row cycle and
#     # column cycle pair and adding their gcd to the cell
#     # count. I've already updated the fixed points count.

# import fractions

# factorials = {}

# def fact(n):
#     global factorials
#     if n in factorials.keys():
#         return factorials[n]
#     product = 1
#     for i in range(1, n+1):
#         product *= i
#         factorials[i] = product
#     return factorials[n]


# def partitions(n):
#     # efficient generator-function found online:
#     # https://jeromekelleher.net/generating-integer-partitions.html
#     a = [0 for i in range(n + 1)]
#     k = 1
#     y = n - 1
#     while k != 0:
#         x = a[k - 1] + 1
#         k -= 1
#         while 2 * x <= y:
#             a[k] = x
#             y -= x
#             k += 1
#         l = k + 1
#         while x <= y:
#             a[k] = x
#             a[l] = y
#             yield a[:k + 2]
#             x += 1
#             y -= 1
#         a[k] = x + y
#         y = x + y - 1
#         yield a[:k + 1]


# def fixed_points_count(col_cycle_type, row_cycle_type, s):
#     independent_cells = 0
#     for col_cycle in col_cycle_type:
#         for row_cycle in row_cycle_type:
#             independent_cells += fractions.gcd(col_cycle, row_cycle)

#     return s**(independent_cells)


# def repeated_term_facts(cycle_type):
#     cycle_length_counts = [1]
#     cycle_type = sorted(cycle_type)
#     for i in range(1, len(cycle_type)):
#         if cycle_type[i] == cycle_type[i-1]:
#             cycle_length_counts[-1] += 1
#         else:
#             cycle_length_counts.append(1)

#     facts_product = 1
#     for count in cycle_length_counts:
#         facts_product *= fact(count)
#     return facts_product


# def perms_with_cycle_type(n, cycle_type):
#     type_product = 1
#     for cycle_length in cycle_type:
#         type_product *= cycle_length

#     overcount_adjuster = repeated_term_facts(cycle_type)

#     return fact(n)/(type_product*overcount_adjuster)


# def perms_with_cycle_types_count(w, h, col_cycle_type, row_cycle_type):
#     col_perm_count = perms_with_cycle_type(w, col_cycle_type)
#     row_perm_count = perms_with_cycle_type(h, row_cycle_type)
#     return col_perm_count*row_perm_count
    

# def solution(w, h, s):
#     # Your code here
#     col_partitions = [part for part in partitions(w)]
#     row_partitions = [part for part in partitions(h)]
    
#     burnside_sum = 0
#     for col_part in col_partitions:
#         for row_part in row_partitions:
#             term = fixed_points_count(col_part, row_part, s)
#             term *= perms_with_cycle_types_count(w, h, col_part, row_part)
#             burnside_sum += term
    
#     burnside_sum /= fact(w)
#     burnside_sum /= fact(h)
#     return str(burnside_sum)

# # answer 7
# print(solution(2, 2, 2))
# # answer 430
# print(solution(2, 3, 4))
















# # first assuming no loops exist, 
#     # they won't help but may confuse things later.
# # also assume choices are inconsequential,
#     # like in the example where sending any variation of
#     # 8 didn't change the result
# # maybe clean the paths first,
#     # remove bad hallways like loops or 
#     # ones from the exits
# # if nothing else is nice we could just simulate it,  (implemented below)
#     # send max amount from entrances each time step, 
#     # let them flow through the network, 
#     # and after n or n+5 steps see how many escape each round.
# # maybe first find all paths from entrances to exits.
# # recursion should work but let's try DP first.
# # maybe first reduce the graph, 
#     # if a room has only one entry and exit
#     # it can be dealt with and removed.
#     # if any loops exist
#     # they can be reduced to one node.
#     # all entrances can reduce to 1 room (implemented)
#     # all exits can reduce to 1 room (implemented)
#     # if two rooms share all sources, they can combine?

# # def sources(room, path):
# #     result = {}
# #     for other_source, row in enumerate(path):
# #         if row[room] != 0:
# #             result.add(other_source)
# #     return result

# def max_outflow(room, path):
#     return sum(path[room])

# def reduce_path(entrances, exits, path):
#     all_rooms = range(len(path))
#     intermediates = []
#     for i in all_rooms:
#         if i in entrances:
#             continue
#         if i in exits:
#             continue
#         intermediates.append(i)
#     new_path = []
#     num_rooms = len(intermediates)+2
#     for i in range(num_rooms):
#         new_path.append([0 for j in range(num_rooms)])
#     # combine all entrances to be room 0
#     # combine all exits to be the last room, -1
#     for source in entrances:
#         for idx, dest in enumerate(intermediates):
#             new_path[0][idx+1] += path[source][dest]
#         for dest in exits:
#             new_path[0][-1] += path[source][dest]
#     for idx_s, source in enumerate(intermediates):
#         for idx_d, dest in enumerate(intermediates):
#             new_path[idx_s+1][idx_d+1] += path[source][dest]
#         for dest in exits:
#             new_path[idx_s+1][-1] += path[source][dest]
#     return new_path



# def solution(entrances, exits, path):
#     # Your code here
#     path = reduce_path(entrances, exits, path)
#     # only entrance is room 0
#     # only exit is room -1
#     # print(path)
#     num_rooms = len(path)
#     room_pop = [0 for room_num in range(num_rooms)]
#     for round_num in range(num_rooms):
#         room_pop_dif = [0 for room_num in range(num_rooms)]
#         for dest, cap in enumerate(path[0]):
#             if dest == num_rooms-1:
#                 num_moving = cap
#             else:
#                 num_moving = min(cap, max_outflow(dest, path)-room_pop[dest])
#             room_pop[dest] += num_moving
#             room_pop_dif[dest] += num_moving
#             # if num_moving > 0:
#             #     print(0, dest, num_moving)
#         for source in sorted(range(1, num_rooms-1), key=(lambda n: room_pop[n]))[::-1]:
#             for dest, cap in sorted(enumerate(path[source]), key=(lambda pair: pair[1]))[::-1]:
#                 if dest == num_rooms-1:
#                     num_moving = min(room_pop[source], cap)
#                 else:
#                     num_moving = min(room_pop[source], cap, max_outflow(dest, path)-room_pop[dest])
#                 # if num_moving > 0:
#                 #     print(source, dest, num_moving)
#                 room_pop[source] -= num_moving
#                 room_pop_dif[source] -= num_moving
#                 room_pop[dest] += num_moving
#                 room_pop_dif[dest] += num_moving
#     return room_pop_dif[-1]

# # answer 6
# print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
# # answer 16
# print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))














# import math
# import fractions

# def reduce_vec(pair):
#     # want (x, y) in reduced form
#     # cannot work if x = y = 0
#     x, y = pair
#     if y == 0:
#         return (int(x/abs(x)), 0)
#     # using for standardizing vectors so vertical up is (0, 1)
#     if x == 0:
#         return (0, int(y/abs(y)))
#     divisor = int(abs(fractions.gcd(x, y)))
#     x, y = x/divisor, y/divisor
#     return (int(x), int(y))

# def solution(dimensions, your_position, trainer_position, distance):
#     #Your code here
#     width, height = dimensions
#     me_x, me_y = your_position
#     t_x, t_y = trainer_position
#     mirror_me_coords = [(me_x, me_y), 
#                         (2*width - me_x, me_y), 
#                         (me_x, 2*height - me_y), 
#                         (2*width - me_x, 2*height - me_y)]
#     mirror_t_coords = [(t_x, t_y), 
#                         (2*width - t_x, t_y), 
#                         (t_x, 2*height - t_y), 
#                         (2*width - t_x, 2*height - t_y)]
#     # me_x + distance < 2*width*mirror_copies_x
#     mirror_copies_x = int(math.ceil((me_x + distance)/(2*width) + 1))
#     # me_y + distance < 2*height*mirror_copies_y
#     mirror_copies_y = int(math.ceil((me_y + distance)/(2*height) + 1))
#     # maybe misnamed but we'll e.g. add mirror_copies_y above *and* below
    
#     shoot_myself_vecs = set()
#     me_distance = {}
#     shoot_trainer_vecs = set()
#     trainer_distance = {}
#     for mirror_idx_x_pos in xrange(mirror_copies_x+2):
#         for mirror_idx_x in [mirror_idx_x_pos, -mirror_idx_x_pos]:
#             for mirror_idx_y_pos in xrange(mirror_copies_y+2):
#                 for mirror_idx_y in [mirror_idx_y_pos, -mirror_idx_y_pos]:
#                     for coords in mirror_me_coords:
#                         mirror_x = coords[0] + mirror_idx_x*2*width
#                         mirror_y = coords[1] + mirror_idx_y*2*height
#                         vec_x = mirror_x - me_x
#                         vec_y = mirror_y - me_y
#                         dist = math.sqrt(vec_x**2 + vec_y**2)
#                         if dist <= distance:
#                             if not (vec_x == 0 and vec_y == 0):
#                                 vec = reduce_vec((vec_x, vec_y))
#                                 if vec not in shoot_myself_vecs:
#                                     shoot_myself_vecs.add(vec)
#                                     me_distance[vec] = dist
#                     for coords in mirror_t_coords:
#                         mirror_x = coords[0] + mirror_idx_x*2*width
#                         mirror_y = coords[1] + mirror_idx_y*2*height
#                         vec_x = mirror_x - me_x
#                         vec_y = mirror_y - me_y
#                         dist = math.sqrt(vec_x**2 + vec_y**2)
#                         if dist <= distance:
#                             vec = reduce_vec((vec_x, vec_y))
#                             if vec not in shoot_trainer_vecs:
#                                 shoot_trainer_vecs.add(vec)
#                                 trainer_distance[vec] = dist
#     good_shots = shoot_trainer_vecs - shoot_myself_vecs
#     for shot in shoot_trainer_vecs & shoot_myself_vecs:
#         if trainer_distance[shot] < me_distance[shot]:
#             good_shots.add(shot)
#     return len(good_shots)

# print(solution([3,2], [1,1], [2,1], 4))
# print(solution([300,275], [150,150], [185,100], 500))
# print(solution([500, 325], [10, 29], [100, 291], 500))