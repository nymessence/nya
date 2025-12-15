#!/usr/bin/env python3
"""
Taygetan Grammar Validator
Validates proper grammatical structures in Taygetan sentences
"""

import re
from typing import List, Dict, Tuple, Optional

class TaygetanGrammarValidator:
    """
    Validates Taygetan grammar against the defined rules
    """
    
    def __init__(self):
        # Case markers and their patterns
        self.case_markers = {
            'genitive': '-en',
            'locative': '-ra', 
            'instrumental': '-sha',
            'dative': '-va',
            'ablative': '-tan',
            'comitative': '-ma'
        }
        
        # Tense markers
        self.tense_markers = {
            'past': '-an',
            'future': '-el', 
            'continuous': '-ra',
            'perfect': '-ta',
            'intensive': '-es'
        }
        
        # Aspect markers
        self.aspect_markers = {
            'imperfective': '-ra',
            'perfective': '-ta',
            'intentive': '-es',
            'habitual': '-na',
            'inceptive': '-sha',
            'cessative': '-men',
            'potential': '-lya'
        }
        
        # Pronouns
        self.pronouns = {
            'singular': ['na', 'ti', 'se'],  # I, you, he/she/they
            'plural': ['ni', 'tu', 'sa'],   # we, you(plural), they
            'honorific': ['nara', 'tira', 'sera'],  # formal versions
            'cosmic': ['nynya', 'teyara', 'samsara']  # cosmic consciousness versions
        }
        
        # Core verbs that should exist in any validation
        self.core_verbs = [
            'lora',  # to exist/be
            'fara',  # to go
            'aya',   # to see/perceive
            'deya',  # to know
            'shira', # to love
            'karma', # to do/work
            'oren',  # to want
            'lo-a'   # to breathe (compound)
        ]
    
    def extract_case_marker(self, word: str) -> Optional[Tuple[str, str]]:
        """
        Extracts case marker from a word if present
        Returns (base_word, case_marker) or None
        """
        word_lower = word.lower()
        
        for case, marker in self.case_markers.items():
            if word_lower.endswith(marker):
                base_word = word_lower[:-len(marker)]
                return base_word, marker
        
        return None
    
    def extract_tense_marker(self, verb: str) -> Optional[Tuple[str, str]]:
        """
        Extracts tense marker from a verb if present
        Returns (base_verb, tense_marker) or None
        """
        verb_lower = verb.lower()
        
        for tense, marker in self.tense_markers.items():
            if verb_lower.endswith(marker):
                base_verb = verb_lower[:-len(marker)]
                return base_verb, marker
        
        return None
    
    def extract_aspect_marker(self, verb: str) -> Optional[Tuple[str, str]]:
        """
        Extracts aspect marker from a verb if present
        Returns (base_verb, aspect_marker) or None
        """
        verb_lower = verb.lower()
        
        for aspect, marker in self.aspect_markers.items():
            if verb_lower.endswith(marker):
                base_verb = verb_lower[:-len(marker)]
                return base_verb, marker
        
        return None
    
    def validate_pronoun_case(self, pronoun_with_case: str) -> Dict[str, any]:
        """
        Validates that a pronoun has appropriate case marking
        """
        result = {
            'valid': True,
            'pronoun': None,
            'case': None,
            'errors': []
        }
        
        # Try to extract case marker
        case_extraction = self.extract_case_marker(pronoun_with_case.lower())
        
        if case_extraction:
            base_form, case_marker = case_extraction
            result['case'] = [k for k, v in self.case_markers.items() if v == case_marker][0]
            
            # Check if the base form is a valid pronoun
            is_valid_pronoun = any(base_form in forms for forms in self.pronouns.values())
            if not is_valid_pronoun:
                result['valid'] = False
                result['errors'].append(f"'{base_form}' is not a valid pronoun base form")
            else:
                result['pronoun'] = base_form
        else:
            # If no case marker, check if the word itself is a valid pronoun
            pronoun_lower = pronoun_with_case.lower()
            is_valid_pronoun = any(pronoun_lower in forms for forms in self.pronouns.values())
            if is_valid_pronoun:
                result['pronoun'] = pronoun_lower
                result['case'] = 'nominative'  # Default case
            else:
                result['valid'] = False
                result['errors'].append(f"'{pronoun_with_case}' is not a valid pronoun")
        
        return result
    
    def validate_verb_conjugation(self, verb: str) -> Dict[str, any]:
        """
        Validates verb for tense and aspect marking
        """
        result = {
            'valid': True,
            'base_verb': None,
            'tense': None,
            'aspect': None,
            'errors': []
        }
        
        # Extract tense marker first
        tense_extraction = self.extract_tense_marker(verb.lower())
        if tense_extraction:
            base_verb, tense_marker = tense_extraction
            result['tense'] = [k for k, v in self.tense_markers.items() if v == tense_marker][0]
        else:
            base_verb = verb.lower()
        
        # Extract aspect marker from the base (or original if no tense)
        aspect_extraction = self.extract_aspect_marker(base_verb)
        if aspect_extraction:
            base_verb, aspect_marker = aspect_extraction
            result['aspect'] = [k for k, v in self.aspect_markers.items() if v == aspect_marker][0]
        
        # Validate the base verb
        is_valid_base = any(base_verb.startswith(cv) for cv in ['l', 'f', 'a', 'd', 's', 'k', 'o', 'lo']) and base_verb in self.core_verbs
        if not is_valid_base:
            # Additional check: look for verbs that might be valid but aren't in core list
            # For now, we'll consider any verb-like structure as potentially valid
            if not re.match(r'^[a-z][a-z]*$', base_verb):
                result['valid'] = False
                result['errors'].append(f"'{base_verb}' does not appear to be a valid verb base")
        
        result['base_verb'] = base_verb
        return result
    
    def validate_sentence_structure(self, sentence: str) -> Dict[str, any]:
        """
        Validates basic sentence structure according to Taygetan word order rules
        """
        result = {
            'valid': True,
            'structure': None,  # OSV, SOV, or VSO
            'elements': [],
            'errors': []
        }
        
        # Split into words and remove punctuation
        words = re.findall(r'\b\w+(?:-\w+)?\b', sentence.lower())
        
        if not words:
            result['valid'] = False
            result['errors'].append("Empty sentence")
            return result
        
        # Identify components by analyzing each word
        components = []
        for word in words:
            # Check if it's a pronoun (with or without case)
            pronoun_check = self.validate_pronoun_case(word)
            if pronoun_check['valid']:
                components.append({'type': 'pronoun', 'word': word, 'info': pronoun_check})
                continue
            
            # Check if it's a verb (with tense/aspect)
            verb_check = self.validate_verb_conjugation(word)
            if verb_check['valid']:
                components.append({'type': 'verb', 'word': word, 'info': verb_check})
                continue
            
            # Otherwise assume it's a noun or other word type
            components.append({'type': 'noun_or_other', 'word': word})
        
        result['elements'] = components
        
        # Try to determine the structure based on component positions
        # This is a simplified analysis
        pronouns = [comp for comp in components if comp['type'] == 'pronoun']
        verbs = [comp for comp in components if comp['type'] == 'verb']
        
        # For the basic validation, we'll check if the sentence follows any of the patterns:
        # 1. OSV - Object Subject Verb
        # 2. SOV - Subject Object Verb  
        # 3. VSO - Verb Subject Object
        
        # If we have at least subject, object, and verb, check the order
        if len(pronouns) >= 1 and len(verbs) >= 1:
            # Check positions
            pronoun_positions = [i for i, comp in enumerate(components) if comp['type'] == 'pronoun']
            verb_positions = [i for i, comp in enumerate(components) if comp['type'] == 'verb']
            
            if len(verb_positions) > 0:
                first_verb_pos = min(verb_positions)
                last_verb_pos = max(verb_positions)
                
                # Check for VSO pattern
                if len(pronoun_positions) >= 2:  # More than one pronoun to have subject and object
                    pronoun_after_verb = [pos for pos in pronoun_positions if pos > first_verb_pos]
                    pronoun_before_verb = [pos for pos in pronoun_positions if pos < first_verb_pos]
                    
                    if len(pronoun_before_verb) > 0 and len(pronoun_after_verb) > 0:
                        # This could be SOV (subject after verb is unlikely but possible in OSV)
                        # If first pronoun is before verb, and there are pronouns after verb, it might be OSV
                        if min(pronoun_before_verb) < first_verb_pos < max(pronoun_after_verb):
                            result['structure'] = 'OSV'
                        elif min(pronoun_after_verb) < first_verb_pos:
                            result['structure'] = 'VSO'
                        else:
                            result['structure'] = 'SOV'
        
        return result
    
    def validate_consciousness_grade(self, word: str) -> Dict[str, any]:
        """
        Validates consciousness-grade reduplication in a word
        """
        result = {
            'valid': True,
            'grade': 1,  # Grade 1 is base form
            'base_word': word,
            'errors': []
        }
        
        # Check for reduplication patterns
        # For example: Nya -> Nynya -> Nynynya -> etc.
        
        # Simple check for vowel-initial reduplication: shira -> shishira -> shishishira
        if len(word) >= 4:
            # Check if it starts with a duplicated syllable
            # This is a simplified check - real validation would be more complex
            lower_word = word.lower()
            
            # Look for patterns like shishira (shi-shira)
            if re.match(r'^([a-z])([a-z]*)\1\2([a-z]+)$', lower_word):
                # This would be something like a-b-a-b where the first part repeats
                result['grade'] = 2
            elif re.match(r'^([a-z])([a-z]*)\1\2\1\2([a-z]+)$', lower_word):
                # This would be a-b-a-b-a-b
                result['grade'] = 3
            elif re.match(r'^([a-z][a-z]*)\1\1([a-z]+)$', lower_word):
                # This would be ab-ab (simpler reduplication)
                result['grade'] = 2
            else:
                # Check for the specific pattern mentioned in the guide: 
                # Nya -> Nynya -> Nynynya
                if lower_word.startswith('ny') and 'nya' in lower_word:
                    if lower_word == 'nya':
                        result['grade'] = 1
                    elif lower_word == 'nynya':
                        result['grade'] = 2
                    elif lower_word == 'nynynya':
                        result['grade'] = 3
                    elif lower_word == 'nynynynya':
                        result['grade'] = 4
                    elif lower_word == 'nynynynynya':
                        result['grade'] = 5
                    elif lower_word == 'nynynynynynya':
                        result['grade'] = 6
                    elif lower_word == 'nynynynynynynya':
                        result['grade'] = 7
                    else:
                        # Not a perfect match, but might be a valid grade pattern
                        # Count how many times the pattern appears
                        # For simplicity, just note that it follows the reduplication pattern
                        pass
                # Check for shira pattern: shira -> shishira -> shishishira
                elif lower_word.startswith('shi') and 'shira' in lower_word:
                    if lower_word == 'shira':
                        result['grade'] = 1
                    elif lower_word == 'shishira':
                        result['grade'] = 2
                    elif lower_word == 'shishishira':
                        result['grade'] = 3
                    elif lower_word == 'shishishishira':
                        result['grade'] = 4
                    elif lower_word == 'shishishishishira':
                        result['grade'] = 5
                    elif lower_word == 'shishishishishishira':
                        result['grade'] = 6
                    elif lower_word == 'shishishishishishishira':
                        result['grade'] = 7
                    else:
                        # Not a perfect match, but might be a valid grade pattern
                        pass
        
        return result

def main():
    validator = TaygetanGrammarValidator()
    
    # Test some basic grammatical structures
    test_sentences = [
        "Na shira Ti",  # I love you (OSV)
        "Ti aya Mira",  # You see stars (OSV)
        "Se fara Dalan",  # He goes home (OSV)
        "Ni lora Te",  # We exist (simple)
        "Na fara-an Dalan-tan",  # I went from home (with case markers)
        "Ti aya-an Shen-en",  # You saw friend's (with case markers)
    ]
    
    print("Taygetan Grammar Validator Test Results:")
    print("=" * 60)
    
    for sentence in test_sentences:
        result = validator.validate_sentence_structure(sentence)
        print(f"Sentence: {sentence}")
        print(f"  Valid: {result['valid']}")
        print(f"  Structure: {result['structure']}")
        print(f"  Elements: {result['elements']}")
        if result['errors']:
            print(f"  Errors: {result['errors']}")
        print()

if __name__ == "__main__":
    main()