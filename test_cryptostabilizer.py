# test_cryptostabilizer.py
"""
Tests for CryptoStabilizer module.
"""

import unittest
from cryptostabilizer import CryptoStabilizer

class TestCryptoStabilizer(unittest.TestCase):
    """Test cases for CryptoStabilizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoStabilizer()
        self.assertIsInstance(instance, CryptoStabilizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoStabilizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
