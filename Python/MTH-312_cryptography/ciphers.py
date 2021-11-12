import random
import sympy
# import math
# import numpy
# import flint


# TODO: comment everything
# TODO: use list.join rather than += for text. more memory efficent
# TODO: plaintext is lowercase, ciphertext is uppercase
# TODO: add "no_repeats=False" and a default repeated char remover


lower_alphabet = ["a", "b", "c", "d", "e", "f", "g",
                  "h", "i", "j", "k", "l", "m",
                  "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

extended_alphabet = lower_alphabet
#for i in ['.', ',', ' ']:
#    extended_alphabet.append(i)

alphabet = extended_alphabet

alpha_to_num: dict = {}
num_to_alpha: dict = {}
dumb_cipher_dict = {}


def make_dictionaries(palphabet=None):
    global alphabet, alpha_to_num, num_to_alpha, dumb_cipher_dict
    if palphabet is not None:
        alphabet = palphabet

    for alphabet_index in range(len(alphabet)):
        alpha_to_num[alphabet[alphabet_index]] = alphabet_index
        num_to_alpha[alphabet_index] = alphabet[alphabet_index]

    for aletter in alphabet:
        dumb_cipher_dict[aletter] = aletter


make_dictionaries()


def remove_repeated_letters(phrase: str) -> str:
    norepeats_phrase = ""
    for letter in phrase:
        if not norepeats_phrase.__contains__(letter):
            norepeats_phrase += letter
    return norepeats_phrase


def encrypt_substitution(plaintext, encryption_dictionary=None,
                         decryption_dictionary=None):
    if encryption_dictionary is None and decryption_dictionary is not None:
        encryption_dictionary = reverse_dictionary(decryption_dictionary)
    if encryption_dictionary is None:
        return plaintext

    ciphertextlist = []
    for letter in plaintext:
        ciphertextlist.append(encryption_dictionary[letter])
    ciphertext = "".join(ciphertextlist)
    return ciphertext


def decrypt_substitution(ciphertext, decryption_dictionary=None,
                         encryption_dictionary=None):
    return encrypt_substitution(ciphertext, decryption_dictionary,
                                encryption_dictionary)


def reverse_dictionary(dictionary):
    reversed_dictionary = {}
    for key in dictionary:
        reversed_dictionary[dictionary[key]] = key
    return reversed_dictionary


def encrypt_random_substitution(plaintext):
    return encrypt_substitution(plaintext, random_dict)


def decrypt_random_substitution(ciphertext):
    return decrypt_substitution(ciphertext, encryption_dictionary=random_dict)


random_dict = {}


def randomize_dict():
    global random_dict
    global alphabet
    randomlist = alphabet.copy()
    random.shuffle(randomlist)
    for index in range(0, len(alphabet)):
        random_dict[alphabet[index]] = randomlist[index]
    return random_dict


randomize_dict()


def encrypt_keyphrase_substitution(plaintext, keyphrase, starting_point=0):
    keyphrase_dict = make_keyphrase_dict(keyphrase, starting_point)
    return encrypt_substitution(plaintext, keyphrase_dict)


def decrypt_keyphrase_substitution(ciphertext, keyphrase, starting_point=0):
    keyphrase_dict = make_keyphrase_dict(keyphrase, starting_point)
    reverse_dict = reverse_dictionary(keyphrase_dict)
    return decrypt_substitution(ciphertext, reverse_dict)


def make_keyphrase_dict(encryption_keyphrase, starting_point=0):
    this_dict = {}
    no_repeats_keyphrase = remove_repeated_letters(encryption_keyphrase)

    for index in range(len(no_repeats_keyphrase)):
        mod_index = (index + starting_point) % len(alphabet)
        this_dict[alphabet[mod_index]] = no_repeats_keyphrase[index]

    alpha_index = starting_point
    unused_alpha_index = 0
    while alphabet[unused_alpha_index] in this_dict.values():
        unused_alpha_index += 1
    while alpha_index < len(alphabet) and unused_alpha_index < len(alphabet):
        if alphabet[alpha_index] not in this_dict:
            this_dict[alphabet[alpha_index]] = alphabet[unused_alpha_index]
            while (unused_alpha_index < len(alphabet) and
                   alphabet[unused_alpha_index] in this_dict.values()):
                unused_alpha_index += 1
        alpha_index = (alpha_index + 1) % len(alphabet)

    return this_dict


def encrypt_shift(plaintext, encryption_key=0, decryption_key=0):
    if encryption_key == 0 and decryption_key != 0:
        encryption_key = -decryption_key
    if encryption_key == 0:
        return plaintext

    ciphertext = ""
    for letter in plaintext:
        plain_num = alpha_to_num[letter]
        cipher_num = (plain_num + encryption_key) % len(alphabet)
        ciphertext += num_to_alpha[cipher_num]
    return ciphertext


def decrypt_shift(ciphertext, decryption_key=0, encryption_key=0):
    return encrypt_shift(ciphertext, decryption_key, encryption_key)


def encrypt_decimation(plaintext, encryption_key=1, decryption_key=1):
    if encryption_key == 1 and decryption_key != 1:
        encryption_key = modular_mult_inverse(decryption_key, len(alphabet))
    if encryption_key == 1:
        return plaintext

    ciphertext = ""
    for letter in plaintext:
        plain_num = alpha_to_num[letter]
        cipher_num = (plain_num * encryption_key) % len(alphabet)
        ciphertext += num_to_alpha[cipher_num]
    return ciphertext


def decrypt_decimation(ciphertext, decryption_key=1, encryption_key=1):
    return encrypt_decimation(ciphertext, decryption_key, encryption_key)


def modular_mult_inverse(num, mod):
    return sympy.mod_inverse(num, mod)


def encrypt_railway(plaintext, num_rails=2):
    ciphertext = ""
    for rail in range(num_rails):
        index = rail
        while index < len(plaintext):
            ciphertext += plaintext[index]
            index += num_rails
    return ciphertext


def decrypt_railway(ciphertext, num_rails):
    plaintext = ""
    rail_lengths = []
    rail_length = len(ciphertext) // num_rails
    for r in range(len(ciphertext) % num_rails):
        rail_lengths.append(rail_length + 1)
    for r in range(len(ciphertext) % num_rails, num_rails):
        rail_lengths.append(rail_length)

    for pos in range(rail_lengths[0]):
        index = pos
        if pos == rail_lengths[0] - 1:
            for length in rail_lengths:
                if length == rail_lengths[0]:
                    plaintext += ciphertext[index]
                    index += length
        else:
            for length in rail_lengths:
                plaintext += ciphertext[index]
                index += length

    return plaintext


def encrypt_columnar_transposition(plaintext, keyword):
    plain_columns = []

    for cols in range(len(keyword)):
        plain_columns.append([])

    plaintext = keyword + plaintext

    col = 0
    for letter in plaintext:
        plain_columns[col].append(letter)
        col = (col + 1) % len(keyword)

    cipher_columns = sorted(plain_columns)
    ciphertext = ""

    for column in cipher_columns:
        column.pop(0)
        for letter in column:
            ciphertext += letter

    return ciphertext


# TODO: give multiple outputs if no_repeats = False?
def decrypt_columnar_transposition(ciphertext, keyword, no_repeats=True):
    if no_repeats:
        keyword = remove_repeated_letters(keyword)
    col_lengths = []
    num_cols = len(keyword)
    col_length = len(ciphertext) // num_cols

    letter_index_list = []
    for x in range(len(keyword)):
        letter_index_list.append([keyword[x], x])
    letter_index_list = sorted(letter_index_list)

    for c in range(num_cols):
        col_lengths.append(0)

    for c in range(len(ciphertext) % num_cols):
        for ind in range(len(letter_index_list)):
            if letter_index_list[ind][1] == c:
                col_lengths[ind] = col_length + 1
    for c in range(len(ciphertext) % num_cols, num_cols):
        for ind in range(len(col_lengths)):
            if not col_lengths[ind]:
                col_lengths[ind] = col_length

    cipher_columns = []
    for columns in range(num_cols):
        cipher_columns.append([])

    index = 0
    for col_index in range(num_cols):
        for letter in range(index, index + col_lengths[col_index]):
            cipher_columns[col_index].append(ciphertext[letter])
        index += col_lengths[col_index]

    sorted_keyword = sorted(keyword)

    index = 0
    for letter in sorted_keyword:
        cipher_columns[index].insert(0, letter)
        index += 1

    plain_columns = []
    for letter in keyword:
        index = 0
        while 0 <= index < len(cipher_columns):
            if cipher_columns[index][0] == letter:
                plain_columns.append(cipher_columns[index])
                cipher_columns.remove(cipher_columns[index])
            index += 1

    plaintext = ""
    for index in range(1, max(col_lengths) + 1):
        if index == max(col_lengths):
            for column in plain_columns:
                if len(column) == max(col_lengths) + 1:
                    plaintext += column[index]
        else:
            for column in plain_columns:
                plaintext += column[index]

    return plaintext


def encrypt_affine(plaintext, a, b):
    ciphertext = plaintext
    ciphertext = encrypt_decimation(ciphertext, a)
    ciphertext = encrypt_shift(ciphertext, b)
    return ciphertext


def decrypt_affine(ciphertext, a, b):
    plaintext = ciphertext
    plaintext = decrypt_shift(plaintext, encryption_key=b)
    plaintext = decrypt_decimation(plaintext, encryption_key=a)
    return plaintext


def encrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    for index in range(len(plaintext)):
        shift = alpha_to_num[keyword[index % len(keyword)]]
        ciphertext += encrypt_shift(plaintext[index], shift)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    for index in range(len(ciphertext)):
        encryption_shift = alpha_to_num[keyword[index % len(keyword)]]
        plaintext += decrypt_shift(ciphertext[index], -encryption_shift)
    return plaintext


def encrypt_vigenere_autokey(plaintext, keyword):
    ciphertext = ""
    key = keyword
    index = 0
    chunk = len(keyword)
    while index < len(plaintext):
        if index + chunk >= len(plaintext):
            ciphertext += encrypt_vigenere(plaintext[index:], key)
        else:
            ciphertext += encrypt_vigenere(plaintext[index: index + chunk],
                                           key)
        key = plaintext[index: index + chunk]
        index += chunk
    return ciphertext


def decrypt_vigenere_autokey(ciphertext, keyword):
    plaintext = ""
    key = keyword
    index = 0
    chunk = len(keyword)
    while index < len(ciphertext):
        if index + chunk >= len(ciphertext):
            plaintext += decrypt_vigenere(ciphertext[index:], key)
        else:
            plaintext += decrypt_vigenere(ciphertext[index: index + chunk],
                                          key)
        key = plaintext[index: index + chunk]
        index += chunk
    return plaintext


# TODO: encrypt playfair
# def encrypt_playfair(plaintext, square=[]):

# TODO: decrypt playfair
# def decrypt_playfair(ciphertext, square=[]):


# TODO: encrypt adfgvx
# def encrypt_adfgvx(plaintext, square=[]):

# TODO: decrypt adfgvx
# def decrypt_adfgvx(ciphertext, square=[]):


def encrypt_hill(plaintext, encryption_matrix=None, decryption_matrix=None):
    if encryption_matrix is None and decryption_matrix is not None:
        decryption_matrix = sympy.Matrix(decryption_matrix)
        encryption_matrix = decryption_matrix.inv_mod(len(alphabet))
    else:
        encryption_matrix = sympy.Matrix(encryption_matrix)

    matrix = sympy.Matrix(encryption_matrix)
    chunk_size = len(matrix.row(0))
    ciphertext = ""

    index = 0
    while index + chunk_size <= len(plaintext):
        letters = plaintext[index: index+chunk_size]
        number_list = [[alpha_to_num[char]] for char in letters]
        letter_vector = sympy.Matrix(number_list)
        cipher_letter_list = matrix.multiply(letter_vector)
        for letter_num in cipher_letter_list:
            ciphertext += num_to_alpha[int(letter_num) % len(alphabet)]
        index += chunk_size

    return ciphertext


def decrypt_hill(ciphertext, decryption_matrix=None, encryption_matrix=None):
    if decryption_matrix is None and encryption_matrix is not None:
        encryption_matrix = sympy.Matrix(encryption_matrix)
        decryption_matrix = encryption_matrix.inv_mod(len(alphabet))
    else:
        decryption_matrix = sympy.Matrix(decryption_matrix)
    return encrypt_hill(ciphertext, decryption_matrix)


if __name__ == '__main__':
    message = "FZGJVAWXWNWPXQE".lower()
    num = "1"
    word = ""
    for digit in num:
        word += num_to_alpha[int(digit)]
    print(decrypt_vigenere(message, word))

