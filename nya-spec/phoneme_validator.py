#!/usr/bin/env python3
"""
Taygetan Phoneme Validator
Validates proper pronunciation of Taygetan phonemes using acoustic models
"""

import re
from typing import List, Dict, Tuple

class TaygetanPhonemeValidator:
    """
    Validates Taygetan phonemes against the defined acoustic models
    """
    
    def __init__(self):
        self.phonemes = {
            'vowels': ['a', 'e', 'i', 'o', 'u', 'y'],
            'consonants': ['n', 't', 's', 'r', 'l', 'f', 'd', 'm', 'sh', 'k'],
            'combinations': ['ny', 'ky', 'ty', 'sy', 'ly', 'my']
        }

        # Define uppercase variants for validation
        self.uppercase_phonemes = {}
        for category, phoneme_list in self.phonemes.items():
            self.uppercase_phonemes[category] = [p.upper() for p in phoneme_list]
        
        # Define valid syllable patterns
        self.valid_patterns = [
            r'[aeiouy]',           # Vowel only (like "a", "i")
            r'[aeiouy][aeiouy]',   # Vowel-Vowel (like "ay", "oi")
            r'[aeiouy][aeiouy][aeiouy]',  # Vowel-Vowel-Vowel (like "aya")
            r'[aeiouy][aeiouy][aeiouy][aeiouy]',  # Extended vowel sequences
            r'[aeiouy][ntsrflmdk]',  # Vowel-Consonant (like "an", "or")
            r'[ntsrflmd][aeiouy]',  # Consonant-Vowel (like "na", "to")
            r'[ntsrflmd][aeiouy][ntsrflmd]',  # Consonant-Vowel-Consonant (like "nat", "tor")
            r'[ntsrflmd](ny|ky|ty|sy|ly|my)[aeiouy]',  # Consonant-Combination-Vowel (like "nya", "kya")
            r'[aeiouy](ny|ky|ty|sy|ly|my)',  # Vowel-Combination (like "anya", "oky")
            r'[ntsrflmd][aeiouy](ny|ky|ty|sy|ly|my)',  # CVC where C is a combination
        ]
    
    def validate_phoneme(self, phoneme: str) -> bool:
        """
        Validates a single phoneme against the defined rules
        """
        # Convert to lowercase for comparison, but preserve original case in logic
        lower_phoneme = phoneme.lower()
        if lower_phoneme in self.phonemes['vowels']:
            return True
        if lower_phoneme in self.phonemes['consonants']:
            return True
        if lower_phoneme in self.phonemes['combinations']:
            return True
        return False
    
    def validate_syllable(self, syllable: str) -> bool:
        """
        Validates a syllable structure according to Taygetan rules
        """
        # Check against valid patterns
        for pattern in self.valid_patterns:
            if re.fullmatch(pattern, syllable):
                return True
        return False
    
    def validate_word(self, word: str) -> Dict[str, any]:
        """
        Validates a complete word and returns validation details
        """
        result = {
            'valid': True,
            'syllables': [],
            'errors': [],
            'phoneme_breakdown': []
        }
        
        # Break word into potential syllables
        syllables = self._segment_word(word)
        
        for i, syllable in enumerate(syllables):
            is_valid = self.validate_syllable(syllable)
            if not is_valid:
                result['valid'] = False
                result['errors'].append(f"Invalid syllable '{syllable}' at position {i}")
            
            result['syllables'].append({
                'syllable': syllable,
                'valid': is_valid
            })
        
        # Check each phoneme in the word
        for phoneme in self._extract_phonemes(word):
            is_valid = self.validate_phoneme(phoneme)
            result['phoneme_breakdown'].append({
                'phoneme': phoneme,
                'valid': is_valid
            })
            
            if not is_valid:
                result['valid'] = False
                result['errors'].append(f"Invalid phoneme '{phoneme}'")
        
        return result
    
    def _segment_word(self, word: str) -> List[str]:
        """
        Naively segments a word into potential syllables
        This is a simplified version - a real implementation would be more sophisticated
        """
        # This is a very basic segmentation algorithm
        # In reality, Taygetan syllable division is more complex
        syllables = []

        # For now, we'll use a simple algorithm looking for vowel sequences
        # and consonant clusters
        vowels = "aeiouy"
        word_lower = word.lower()

        i = 0
        while i < len(word_lower):
            # Find the start of a vowel group
            while i < len(word_lower) and word_lower[i] not in vowels:
                i += 1

            if i >= len(word_lower):
                break

            # Capture vowel sequence
            vowel_start = i
            while i < len(word_lower) and word_lower[i] in vowels:
                i += 1
            vowel_seq = word[vowel_start:i]  # Use original case from word

            # Capture consonant cluster after vowels
            consonant_end = i
            while i < len(word_lower) and word_lower[i] not in vowels:
                # Check for combinations like 'ny', 'ky', etc.
                if i + 1 < len(word_lower) and word_lower[i:i+2] in self.phonemes['combinations']:
                    i += 2
                else:
                    i += 1
            consonant_seq = word[consonant_end:i]  # Use original case from word

            # Combine to form syllable
            syllable = vowel_seq + consonant_seq
            syllables.append(syllable)

        return syllables
    
    def _extract_phonemes(self, word: str) -> List[str]:
        """
        Extracts individual phonemes from a word
        """
        phonemes = []
        i = 0
        word_lower = word.lower()  # Convert to lowercase for comparison

        while i < len(word_lower):
            # Check for two-character consonant combinations first (like 'sh')
            if i + 1 < len(word_lower) and word_lower[i:i+2] in self.phonemes['consonants']:
                phonemes.append(word[i:i+2])  # Use original case from word
                i += 2
            # Check for two-character combinations (like 'ny', 'ky', etc.)
            elif i + 1 < len(word_lower) and word_lower[i:i+2] in self.phonemes['combinations']:
                phonemes.append(word[i:i+2])  # Use original case from word
                i += 2
            # Check for single characters
            elif word_lower[i] in self.phonemes['vowels'] or word_lower[i] in self.phonemes['consonants']:
                phonemes.append(word[i])  # Use original case from word
                i += 1
            else:
                # Handle unrecognized characters
                phonemes.append(word[i])
                i += 1
        return phonemes

def main():
    validator = TaygetanPhonemeValidator()
    
    # Test some basic words
    test_words = [
        "Nya",      # Should be valid: N-ya (Consonant-Combination-Vowel)
        "Shira",    # Should be valid: Shi-ra
        "Tora",     # Should be valid: To-ra  
        "Mira",     # Should be valid: Mi-ra
        "Fara",     # Should be valid: Fa-ra
        "invalid"   # Should be invalid
    ]
    
    print("Taygetan Phoneme Validator Test Results:")
    print("=" * 50)
    
    for word in test_words:
        result = validator.validate_word(word)
        print(f"Word: {word}")
        print(f"  Valid: {result['valid']}")
        print(f"  Syllables: {result['syllables']}")
        print(f"  Phoneme Breakdown: {result['phoneme_breakdown']}")
        if result['errors']:
            print(f"  Errors: {result['errors']}")
        print()

if __name__ == "__main__":
    main()