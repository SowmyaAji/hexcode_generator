import unittest
from generate_hex import get_hex, validate_common, validate_sequences, generate_hashed_string

class TestHexCodes(unittest.TestCase):
    def test_get_hex(self):
        self.assertEqual(len(get_hex()), 8, f"Should be 8 not { len(get_hex())} ")
        
    def test_validate_common(self):
        self.assertTrue(validate_common("DEADCELL"),f"Does not exist in common magic hexcodes used by industry")
        
    def test_validate_common_false(self):
        self.assertFalse(validate_common("32E716BA"),f"It exists in common magic hexcodes used by industry")
        
    def test_validate_sequences(self):
        self.assertFalse(validate_sequences("12345678"), f"This does not contain a sequence")
        
    def test_validate_sequences(self):
        self.assertFalse(validate_sequences("AAAAAAAA"), f"This does not contain a sequence and is valid")
        
    def test_validate_sequences(self):
        self.assertTrue(validate_sequences("32E716BA"), f"This contains a sequence and is not valid")
        
    def test_generate_hashed_string(self):
        self.assertEqual(len(generate_hashed_string("32E716BA")), 64, f" Length should be 64, not {len(generate_hashed_string('32E716BA'))}")

if __name__ == '__main__':
    unittest.main()