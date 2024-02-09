import unittest
from dice_game_api import app

class TestDiceGame(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True

  def test_get_probabilities_list(self):
    # Test getting the list of probabilities without providing 'k'
    response = self.app.get('/getProbability')
    self.assertEqual(response.status_code, 200)
    self.assertIn('res', response.json)
    self.assertEqual(len(response.json['res']), 94) # Since we expect probabilities for k=6 through 99

  def test_get_single_probability(self):
    # Test getting a single probability by providing 'k' in the header
    k_value = 10
    response = self.app.get('/getProbability', headers={'k': str(k_value)})
    self.assertEqual(response.status_code, 200)
    self.assertIn('res', response.json)
    self.assertIsInstance(response.json['res'], float)

  def test_invalid_k_value(self):
    # Test the response for an invalid 'k' value
    response = self.app.get('/getProbability', headers={'k': 'invalid'})
    self.assertEqual(response.status_code, 400)
    self.assertIn('error', response.json)

if __name__ == '__main__':
  unittest.main()
