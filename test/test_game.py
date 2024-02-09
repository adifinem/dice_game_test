import unittest
from dice_game import get_probability_list

class TestBobWinningProbability(unittest.TestCase):

  def test_probability_structure(self):
    """Test that the output is a list of correct length with probabilities for k=6 to k=99."""
    probabilities = get_probability_list()
    self.assertIsInstance(probabilities, list, "Output should be a list.")
    self.assertEqual(len(probabilities), 94, "Output list should contain 94 elements for k=6 to k=99.")

  def test_probability_values(self):
    """Test subset of pre-calculated probability values to ensure correctness."""
    probabilities = get_probability_list()
    self.assertAlmostEqual(probabilities[0], 0.545454, places=5, msg="Probability for k=6 does not match expected value.")
    self.assertAlmostEqual(probabilities[1], 0.538461, places=5, msg="Probability for k=7 does not match expected value.")
    self.assertAlmostEqual(probabilities[2], 0.533333, places=5, msg="Probability for k=8 does not match expected value.")
    self.assertAlmostEqual(probabilities[3], 0.529411, places=5, msg="Probability for k=9 does not match expected value.")

  def test_probability_range(self):
    """Test that all probabilities are in the range (0, 1)."""
    probabilities = get_probability_list()
    for p in probabilities:
      self.assertTrue(0 < p < 1, "Each probability should be between 0 and 1.")

if __name__ == '__main__':
  unittest.main()

