import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from src.converter import MorseCodeConverter

class TestMorseConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MorseCodeConverter()

    def test_simple_word(self):
        # Tes kata sederhana
        result = self.converter.text_to_morse("SOS")
        self.assertEqual(result, "... --- ...")

    def test_with_numbers(self):
        # Tes angka
        result = self.converter.text_to_morse("A1")
        self.assertEqual(result, ".- .----")

    def test_lowercase_input(self):
        # Tes apakah huruf kecil otomatis dikonversi (karena ada clean_text)
        result = self.converter.text_to_morse("abc")
        self.assertEqual(result, ".- -... -.-.")

    def test_special_characters_removal(self):
        # Tes apakah karakter aneh dihapus tanpa merusak program
        result = self.converter.text_to_morse("HELLO!")
        self.assertEqual(result, ".... . .-.. .-.. ---")

if __name__ == "__main__":
    unittest.main()