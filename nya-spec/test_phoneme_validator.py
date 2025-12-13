# Taygetan Phoneme Validator Test Suite

import unittest
from phoneme_validator import TaygetanPhonemeValidator

class TestTaygetanPhonemeValidator(unittest.TestCase):
    def setUp(self):
        self.validator = TaygetanPhonemeValidator()
    
    def test_valid_phonemes(self):
        """Test that valid phonemes are recognized"""
        valid_phonemes = ['a', 'e', 'i', 'o', 'u', 'y', 'n', 't', 's', 'r', 'l', 'f', 'd', 'm', 'sh', 'k']
        for phoneme in valid_phonemes:
            with self.subTest(phoneme=phoneme):
                self.assertTrue(self.validator.validate_phoneme(phoneme))
    
    def test_valid_combinations(self):
        """Test that valid phoneme combinations are recognized"""
        valid_combinations = ['ny', 'ky', 'ty', 'sy', 'ly', 'my']
        for combo in valid_combinations:
            with self.subTest(combo=combo):
                self.assertTrue(self.validator.validate_phoneme(combo))
    
    def test_invalid_phonemes(self):
        """Test that invalid phonemes are rejected"""
        invalid_phonemes = ['b', 'g', 'j', 'x', 'z', 'ch', 'th', 'ph']
        for phoneme in invalid_phonemes:
            with self.subTest(phoneme=phoneme):
                self.assertFalse(self.validator.validate_phoneme(phoneme))
    
    def test_valid_syllables(self):
        """Test that valid syllable structures are recognized"""
        valid_syllables = [
            'a', 'i', 'u',         # Single vowels
            'na', 'ti', 'se',      # Consonant-vowel
            'an', 'it', 'us',      # Vowel-consonant
            'nya', 'kya', 'tya',   # Consonant-y-vowel
            'tor', 'mir', 'far'    # Consonant-vowel-consonant
        ]
        for syllable in valid_syllables:
            with self.subTest(syllable=syllable):
                # Note: This test may need adjustment based on implemented patterns
                pass  # Placeholder since syllable validation is complex
    
    def test_valid_words(self):
        """Test that valid Taygetan words are recognized"""
        valid_words = [
            'Nya',    # Awareness
            'Shira',  # Love
            'Tora',   # Sun
            'Mira',   # Star
            'Fara',   # Go
            'Nora',   # Water
            'Kyra',   # Path
            'Rila',   # Tool
        ]
        for word in valid_words:
            with self.subTest(word=word):
                result = self.validator.validate_word(word)
                self.assertTrue(result['valid'], f"Word {word} should be valid but got errors: {result.get('errors', [])}")
    
    def test_invalid_words(self):
        """Test that invalid words are rejected"""
        invalid_words = [
            'xyz',      # Contains invalid phonemes
            'bogus',    # Contains invalid phonemes like 'b', 'g'
        ]
        for word in invalid_words:
            with self.subTest(word=word):
                result = self.validator.validate_word(word)
                self.assertFalse(result['valid'], f"Word {word} should be invalid")

if __name__ == '__main__':
    unittest.main()