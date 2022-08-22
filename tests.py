
import unittest
from generate_hex import get_hex, validate_common, validate_sequences, generate_hashed_string, validate_common, validate_not_used
from unittest.mock import MagicMock, patch

class TestHexCodes(unittest.TestCase):
    def test_get_hex(self):
        self.assertEqual(len(get_hex()), 8, f"Should be 8 not { len(get_hex())} ")
        
    def test_validate_common(self):
        self.assertTrue(validate_common("DEADCELL"),f"Does not exist in common magic hexcodes used by industry")
        
    def test_validate_common_false(self):
        self.assertFalse(validate_common("32E716BA"),f"It exists in common magic hexcodes used by industry")
        
    def test_validate_sequences_one(self):
        self.assertFalse(validate_sequences("12345678"), f"This does not contain a sequence")
        
    def test_validate_sequences_two(self):
        self.assertFalse(validate_sequences("AAAAAAAA"), f"This does not contain a sequence and is valid")
        
    def test_validate_sequences_three(self):
        self.assertTrue(validate_sequences("32E716BA"), f"This contains a sequence and is not valid")
        
    def test_generate_hashed_string(self):
        self.assertEqual(len(generate_hashed_string("32E716BA")), 64, f" Length should be 64, not {len(generate_hashed_string('32E716BA'))}")
    
    def test_validate_not_used_insert(self):
        with patch('generate_hex.sqlite3') as conn:
            res = validate_not_used(conn, "1DB06C53", "831e33be1b6f6bfe7356664a9cf088b3722371f1e38bc575781b216db2508b00", 3)
            self.assertEqual(res, "1DB06C53", f"Failed to insert hashcode into db")

if __name__ == '__main__':
    unittest.main()