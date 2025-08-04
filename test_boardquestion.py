# test_boardquestion.py
"""
Tests for BoardQuestion module.
"""

import unittest
from boardquestion import BoardQuestion

class TestBoardQuestion(unittest.TestCase):
    """Test cases for BoardQuestion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BoardQuestion()
        self.assertIsInstance(instance, BoardQuestion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BoardQuestion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
