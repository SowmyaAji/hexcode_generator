
import unittest
from generate_hex import get_hex, validate_common, validate_sequences, generate_hashed_string, validate_common, validate_not_used
from unittest.mock import patch
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
        with patch('db.sqlite3') as conn:
            results = []
            res = validate_not_used(conn, "1DB06C53", "831e33be1b6f6bfe7356664a9cf088b3722371f1e38bc575781b216db2508b00", results, conn.cursor(), 3)
            self.assertEqual(res, "1DB06C53", f"Failed to insert hashcode into db")
            

    def test_validate_not_used(self):
        with patch('db.sqlite3') as conn:
            results = [("831e33be1b6f6bfe7356664a9cf088b3722371f1e38bc575781b216db2508b00",)]
            res = validate_not_used(conn, "1DB06C53", "831e33be1b6f6bfe7356664a9cf088b3722371f1e38bc575781b216db2508b00", results, conn.cursor(), 3)
            self.assertEqual(res, "Hex code already used earlier", f"Hashcode not in db")
            
    def test_validate_not_used_drop(self):
        with patch('db.sqlite3') as conn:
            results = [("7b4379d483c3059191bb1370e059bd20a2be60b8c64d9e26cc942322a7d849cf",),("3106bed73654e22e91408787b28c1a5dd6d8fad82db74d6d5257c3425e8949b0", ),
                        ("f97b17e884efcb66c97022ce119259350ab806ec51d1e263d118252536c2e44a",)]
            res = validate_not_used(conn, "1DB06C53", "831e33be1b6f6bfe7356664a9cf088b3722371f1e38bc575781b216db2508b00", results, conn.cursor(), 3)
            self.assertEqual(res, "All valid hexcodes exhausted, restarting ...", f"All unique codes are not done")
        

if __name__ == '__main__':
    unittest.main()