import math
import unittest

import hm3_315780122 as hm3
import test

class TestHm3(unittest.TestCase):
    def test_bin_to_fraction(self):
        self.assertEqual(0.40625, hm3.bin_to_fraction('01101'))
        self.assertEqual(0.5, hm3.bin_to_fraction('1'))
        self.assertEqual(0.75, hm3.bin_to_fraction('11'))
        self.assertEqual(0.875, hm3.bin_to_fraction('111'))
        self.assertEqual(0.625, hm3.bin_to_fraction('1010000'))

    def test_bin_to_float(self):
        self.assertEqual(0.15625, hm3.bin_to_float('00111110001000000000000000000000'))
        self.assertEqual(2, hm3.bin_to_float('01000000000000000000000000000000'))
        self.assertEqual(-2, hm3.bin_to_float('11000000000000000000000000000000'))
        self.assertEqual(-36893488147419103232, hm3.bin_to_float('11100000000000000000000000000000'))
        self.assertEqual(-118842243771396506390315925504, hm3.bin_to_float('111011111100000000000000000000000'))

    def test_is_greater_equal(self):

        self.assertEqual(False, hm3.is_greater_equal('00111110001000000000000000000000', '00111111001000000000000000000000'))
        self.assertEqual(True, hm3.is_greater_equal('00111110001000000000000000000000', '00111110001000000000000000000000'))
        self.assertEqual(True, hm3.is_greater_equal('11000000010000000000000000000000', '11000000011000000000000000000000'))
        self.assertEqual(False, hm3.is_greater_equal('11000000110000000000000000000000', '11000000011000000000000000000000'))
        self.assertEqual(True, hm3.is_greater_equal('11000000011000000000000000000000', '11000000110000000000000000000000'))
        self.assertEqual(False, hm3.is_greater_equal('11000000110000000000000000000000', '01000000011000000000000000000000'))
        self.assertEqual(True, hm3.is_greater_equal('01000000110000000000000000000000', '11000000011000000000000000000000'))

    def test_approx_root(self):
        self.assertEqual(([1, 3], 1.3333333333333333), hm3.approx_root(2, 0.1))
        self.assertEqual(([1, 1, 5], 2.2), hm3.approx_root(5, 0.1))
        self.assertEqual(([1, 1, 1], 3), hm3.approx_root(9, 0.1))
        self.assertEqual(([1, 1, 3, 3], 2.4444444444444446), hm3.approx_root(6, 0.1))
        self.assertEqual(([1, 1, 2, 2], 2.75), hm3.approx_root(8, 0.1))
        self.assertEqual(([1, 1, 2, 2, 4, 4], 2.828125), hm3.approx_root(8, 0.01))
        self.assertEqual(([1, 3, 5, 5, 16, 18, 78], 1.4142135565052232), hm3.approx_root(2, 0.00000001))
        self.assertEqual(([1, 1, 5, 6, 13, 16, 16, 38, 48, 58, 104, 179], 2.2360679774997894), hm3.approx_root(5, 0.000000000000001))



    def test_approx_e(self):
        self.assertEqual(True, abs(math.e - hm3.approx_e(100)) < 0.3)
        self.assertEqual(True, abs(math.e - hm3.approx_e(1000)) < 0.2)
        self.assertEqual(True, abs(math.e - hm3.approx_e(10000)) < 0.1)

    def test_find(self):
        self.assertEqual(3, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 5))
        self.assertEqual(0, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 2))
        self.assertEqual(1, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 1))
        self.assertEqual(2, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 3))
        self.assertEqual(4, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 4))
        self.assertEqual(5, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 7))
        self.assertEqual(6, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 6))
        self.assertEqual(7, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 8))
        self.assertEqual(8, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 9))
        self.assertEqual(None, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 0))
        self.assertEqual(None, hm3.find([2, 1, 3, 5, 4, 7, 6, 8, 9], 10))
        self.assertEqual(0, hm3.find([2, 1, 3], 2))
        self.assertEqual(3, hm3.find([2, 1, 3, 5], 5))
        self.assertEqual(1, hm3.find([2, 1], 1))

    def test_sort_from_almost(self):
        lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], hm3.sort_from_almost(lst))

        lst = [2, 1, 4, 3, 6, 5, 8, 7, 9]

        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], hm3.sort_from_almost(lst))

        lst = [1, 1, 1, 1, 1, 2, 1]

        self.assertEqual([1, 1, 1, 1, 1, 1, 2], hm3.sort_from_almost(lst))

        lst = [2, 1]

        self.assertEqual([1, 2], hm3.sort_from_almost(lst))

    def test_find_local_min(self):

        self.assertEqual(4, hm3.find_local_min([5, 4, 3, 2, 1, 2, 3, 4, 5]))
        self.assertEqual(3, hm3.find_local_min([5, 4, 3, 1, 2, 2.5, 3, 4, 5]))
        self.assertEqual(2, hm3.find_local_min([5, 4, 1, 2, 2.5, 2.75, 3, 4, 5]))
        self.assertEqual(1, hm3.find_local_min([5, 1, 2.1, 2.2, 2.3, 2.4, 3, 4, 5]))
        self.assertEqual(0, hm3.find_local_min([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(6, hm3.find_local_min([7, 6, 5, 4, 3, 2, 1]))



    def test_injective_func(self):
        str1 = "aaaaaaaaa"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "abaaaaaaa"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "aacaaaaaa"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "aaadaaaaa"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "aaaaaeaaa"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "aaaaaeeaa"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "aaaaaeaea"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "eaaaaeaae"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "eeeeeeeee"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "ddeeccaab"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "abcdeabcd"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))
        str1 = "aede"
        self.assertEqual(str1, hm3.int_to_string(len(str1), hm3.string_to_int(str1)))



    def test_sort_strings1(self):
        lst1 = ["eee", "ddd", "ccc", "bbb", "aaa"]
        self.assertEqual(lst1[::-1], hm3.sort_strings1(lst1, 3))
        lst1 = ["eee", "edc", "ecb", "eba", "eee"]
        self.assertEqual(["eba", "ecb", "edc", "eee", "eee"], hm3.sort_strings1(lst1, 3))
        lst1 = ["eee", "eac", "eab", "eaa", "eee"]
        self.assertEqual(["eaa", "eab", "eac", "eee", "eee"], hm3.sort_strings1(lst1, 3))
        lst1 = ["aae", "aad", "aad", "aac", "aab"]
        self.assertEqual(["aab", "aac", "aad", "aad", "aae"], hm3.sort_strings1(lst1, 3))
        lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
        self.assertEqual(['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea'], hm3.sort_strings1(lst1, 4))
        lst1 = ['aaec', 'abcd', 'dcba', 'bacd', 'cdab', 'cccc', 'cccb', 'eded', 'dede', 'abca']
        self.assertEqual(['aaec', 'abca', 'abcd', 'bacd', 'cccb', 'cccc', 'cdab', 'dcba', 'dede', 'eded'], hm3.sort_strings1(lst1, 4))


    def test_sort_strings2(self):
        lst1 = ["eee", "ddd", "ccc", "bbb", "aaa"]
        self.assertEqual(lst1[::-1], hm3.sort_strings2(lst1, 3))
        lst1 = ["eee", "edc", "ecb", "eba", "eee"]
        self.assertEqual(["eba", "ecb", "edc", "eee", "eee"], hm3.sort_strings2(lst1, 3))
        lst1 = ["eee", "eac", "eab", "eaa", "eee"]
        self.assertEqual(["eaa", "eab", "eac", "eee", "eee"], hm3.sort_strings2(lst1, 3))
        lst1 = ["aae", "aad", "aad", "aac", "aab"]
        self.assertEqual(["aab", "aac", "aad", "aad", "aae"], hm3.sort_strings2(lst1, 3))
        lst1 = ["aae", "aad", "aad", "aac", "aab"]
        self.assertEqual(["aab", "aac", "aad", "aad", "aae"], hm3.sort_strings2(lst1, 3))
        lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
        self.assertEqual(['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea'], hm3.sort_strings2(lst1, 4))
        lst1 = ['aaec', 'abcd', 'dcba', 'bacd', 'cdab', 'cccc', 'cccb', 'eded', 'dede', 'abca']
        self.assertEqual(['aaec', 'abca', 'abcd', 'bacd', 'cccb', 'cccc', 'cdab', 'dcba', 'dede', 'eded'], hm3.sort_strings2(lst1, 4))


   
