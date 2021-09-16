# TODO: letter frequencies against known english ones
# TODO: and digraph, trigraph, etc

# TODO: chart and list output
# TODO: common positions/relationships for groups of letters?
# TODO: plaintext attack (known cipher and a couple letters)
# TODO: vigenere multiple frequency analysis
# TODO: vigenere autokey analysis?
# TODO: automated or manual kasiski attack


from MTH_312 import ciphers as c


def load_words():
    valid_words = []
    with open('1k.txt') as word_file:
        for line in word_file:
            valid_words.append(line[:-1])

    return valid_words


top_words = load_words()
longest_word = ""
for word in top_words:
    if len(word) > len(longest_word):
        longest_word = word


def count_words(test_text, min_length=1):
    count = 0
    matches = []
    for index in range(0, len(test_text)):
        for window in range(min_length, len(longest_word)):
            if index + window <= len(test_text):
                this_word = test_text[index: index + window]
                if this_word in top_words:
                    count += len(this_word)
                    matches.append(this_word)
    return count, matches


def check_shift(ciphertext, min_length=1):
    max_matches = 0
    best_shift = 0
    matches = []
    for shift in range(len(c.alphabet)):
        this_count, this_matches = count_words(c.decrypt_shift(ciphertext, encryption_key=shift), min_length)
        if this_count > max_matches:
            max_matches = this_count
            best_shift = shift
            matches = this_matches
    return c.decrypt_shift(ciphertext, encryption_key=best_shift), f"encryption shift: {best_shift}", f"matched letters: {max_matches}", f"matched words: {matches}"


def check_decimation(ciphertext, min_length=1):
    max_matches = 0
    best_mult = 0
    matches = []
    for mult in range(1, len(c.alphabet)):
        this_count, this_matches = count_words(c.decrypt_decimation(ciphertext, encryption_key=mult), min_length)
        if this_count > max_matches:
            max_matches = this_count
            best_mult = mult
            matches = this_matches
    return c.decrypt_decimation(ciphertext, encryption_key=best_mult), f"encryption multiplier: {best_mult}", f"matched letters: {max_matches}", f"matched words: {matches}"


def check_affine(ciphertext, min_length=1):
    max_matches = 0
    best_ab = [0, 0]
    matches = []
    for mult in range(1, len(c.alphabet)):
        for shift in range(len(c.alphabet)):
            this_count, this_matches = count_words(c.decrypt_affine(ciphertext, mult, shift), min_length)
            if this_count > max_matches:
                max_matches = this_count
                best_ab = [mult, shift]
                matches = this_matches
    return c.decrypt_affine(ciphertext, best_ab[0], best_ab[
        1]), f"encryption (a, b): {best_ab}", f"matched letters: {max_matches}", f"matched words: {matches}"


# def check_hill(ciphertext, size, min_length=1):
#     max_matches = 0
#     best_matrix = []
#     temp_matrix = []
#     for row in range(size):
#         temp_matrix.append([])
#         for column in range(size):
#             temp_matrix[-1].append(0)
#
#     # for row in range(size):
#     #     for column in range(size):
#     #         temp_matrix[row][column]
#     #         this_count =

cipher_text = "this is a test".lower()
print(check_affine(cipher_text))
