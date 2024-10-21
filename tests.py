import unittest
from boggle_solver import Boggle

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  def test_Words_That_Only_Are_3_or_More_Chars(self):
    """
    Ensure that words shorter than 3 characters are not included.
    """
    grid = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    dictionary = ["AB", "ABC", "GHEFI"]
    boggle = Boggle(grid, dictionary)
    
    # Expected words are those with at least 3 characters
    expected = ["ABC", "GHEFI"]
    
    result = boggle.getSolution()
    
    # Debugging output to verify results
    print(f"Result: {result}")
    
    self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()
