# test_insightbridge.py
"""
Tests for InsightBridge module.
"""

import unittest
from insightbridge import InsightBridge

class TestInsightBridge(unittest.TestCase):
    """Test cases for InsightBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InsightBridge()
        self.assertIsInstance(instance, InsightBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InsightBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
