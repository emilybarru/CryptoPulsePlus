# test_cryptopulseplus.py
"""
Tests for CryptoPulsePlus module.
"""

import unittest
from cryptopulseplus import CryptoPulsePlus

class TestCryptoPulsePlus(unittest.TestCase):
    """Test cases for CryptoPulsePlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoPulsePlus()
        self.assertIsInstance(instance, CryptoPulsePlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoPulsePlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
