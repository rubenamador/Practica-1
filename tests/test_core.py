# -*- coding: utf-8 -*-

from .context import sample

import unittest
import collections
from collections import Counter

class CoreTestSuite(unittest.TestCase):
    """Test cases for Core"""

    def test_count(self):
        # SET-UP
        sentence = "str"

        # EXECUTION
        result = sample.count(sentence)

        # ASSERT
        self.assertEqual(sample.count('pepe y otilio'), Counter({'pepe': 1, 'otilio': 1, 'y': 1}))

    def test_count_three_different_words(self):
     self.assertEqual(sample.count('pepe y otilio'), Counter({'pepe': 1, 'otilio': 1, 'y': 1}))
	 
    def test_count_three_equal_words(self):
     self.assertEqual(sample.count('mariano mariano mariano'), Counter({'mariano': 3}))
	 
    def test_count_three_equal_words_with_mix_of_minus_and_mayus(self):
     self.assertEqual(sample.count('Jose jOSe josE'), Counter({'jose': 3}))

    def test_count_ascii_two_different_words_with_mix_of_minus_and_mayus_with_repetitions(self):
     self.assertEqual(sample.count('KaZuYa verSus KazuYa VersUs Kazuya VersuS KAZUYA'), Counter({'kazuya': 4, 'versus': 3}))

    def test_count_unicode(self):
     self.assertEqual(sample.count(u'KaZuYa verSus KazuYa VersUs Kazuya VersuS KAZUYA'), Counter({'kazuya': 4, 'versus': 3}))
 
    def test_count_latin_1(self):
     self.assertEqual(sample.count(b'KaZuYa verSus KazuYa VersUs Kazuya VersuS KAZUYA'), Counter({b'kazuya': 4, b'versus': 3}))

    def test_count_unicode2(self):
     self.assertEqual(sample.count(r'KaZuYa verSus KazuYa VersUs Kazuya VersuS KAZUYA'), Counter({'kazuya': 4, 'versus': 3}))

    def test_count_double_spaces(self):
     self.assertEqual(sample.count('KaZuYa  verSus    KazuYa  VersUs   Kazuya  VersuS  KAZUYA'), Counter({'kazuya': 4, 'versus': 3}))

    def test_count_with_tabs(self):
     self.assertEqual(sample.count('KaZuYa	verSus	KazuYa	VersUs	Kazuya	VersuS	KAZUYA.'), Counter({'kazuya': 4, 'versus': 3}))

if __name__ == '__main__':
    unittest.main()
