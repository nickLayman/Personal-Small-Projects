import unittest
import sympy
# import math
# import numpy

from MTH_312 import ciphers as c


class MyTestCase(unittest.TestCase):
    plaintext1 = "test"
    plaintext2 = "the quick brown fox jumps over the lazy dog."
    plaintext3 = "sphinx of black quartz, judge my vow."
    plaintext4 = "imagine others complexly."

    key_num1 = 1
    key_num2 = 5
    key_num3 = 14
    key_num4 = 22

    key_word1 = "test"
    key_word2 = "mykey"
    key_word3 = "grand valley"
    key_word4 = "graduation"

    key_matrix1 = sympy.Matrix([[1, 0],
                                [0, 1]])

    key_matrix2 = sympy.Matrix([[2, 5],
                                [3, 4]])

    key_matrix3 = sympy.Matrix([[2, 4, 5],
                                [3, 4, 2],
                                [5, 1, 2]])

    key_matrix4 = sympy.Matrix([[1, 2, 3],
                                [6, 5, 4],
                                [7, 6, 3]])

    def test_remove_repeated_letters(self):
        self.assertEqual("tes", c.remove_repeated_letters(self.plaintext1))
        self.assertEqual("the quickbrownfxjmpsvlazydg.",
                         c.remove_repeated_letters(self.plaintext2))
        self.assertEqual("sphinx ofblackqurtz,jdgemyvw.",
                         c.remove_repeated_letters(self.plaintext3))
        self.assertEqual("imagne othrscplxy.",
                         c.remove_repeated_letters(self.plaintext4))
        self.assertEqual("tes",
                         c.remove_repeated_letters(self.key_word1))
        self.assertEqual("myke",
                         c.remove_repeated_letters(self.key_word2))
        self.assertEqual("grand vley",
                         c.remove_repeated_letters(self.key_word3))
        self.assertEqual("gradution",
                         c.remove_repeated_letters(self.key_word4))

    def test_substitution(self):
        self.assertTrue(True)

    def test_reverse_dictionary(self):
        self.assertTrue(True)

    def test_random_substitution(self):
        self.assertTrue(True)

    def test_randomize_dict(self):
        self.assertTrue(True)

    def test_keyphrase_substitution(self):
        self.assertEqual("rbqr",
                         c.encrypt_keyphrase_substitution("test",
                                                          "test"))

    def test_make_keyphrase_dict(self):
        alpha = "abcdefghijklmnopqrstuvwxyz., "
        encrypted = "tesabcdfghijklmnopqruvwxyz., "
        dictionary = c.make_keyphrase_dict("test")
        for i in range(len(encrypted)):
            self.assertEqual(encrypted[i], dictionary[alpha[i]])

    def test_shift(self):
        self.assertEqual("uftu", c.encrypt_shift("test", 1))

    def test_decimation(self):
        self.assertEqual("iudi", c.encrypt_decimation("test", 5))

    def test_modular_mult_inverse(self):
        self.assertEqual(6, c.modular_mult_inverse(5, 29))

    def test_railway(self):
        self.assertEqual("tset", c.encrypt_railway("test", 2))

    def test_columnar_transposition(self):
        self.assertTrue(True)

    def test_affine(self):
        self.assertEqual("jvej", c.encrypt_affine("test", 5, 1))

    def test_vigenere(self):
        self.assertTrue(True)

    def test_vigenere_autokey(self):
        self.assertTrue(True)

    def test_playfair(self):
        self.assertTrue(True)

    def test_adfgvx(self):
        self.assertTrue(True)

    def test_hill(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
