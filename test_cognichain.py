# test_cognichain.py
"""
Tests for CogniChain module.
"""

import unittest
from cognichain import CogniChain

class TestCogniChain(unittest.TestCase):
    """Test cases for CogniChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CogniChain()
        self.assertIsInstance(instance, CogniChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CogniChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
