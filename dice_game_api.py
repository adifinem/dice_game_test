from flask import Flask, request, jsonify

app = Flask(__name__)
from dice_game import calculate_bob_winning_probability, get_probability_list

@app.route('/getProbability', methods=['GET'])
def get_probability():
  # Check if "k" header is provided
  k = request.headers.get('k')
  if k:
    try:
      k = int(k)
      # Ensure k is within the allowed range
      if k < 6 or k > 99:
        return jsonify({"error": "k must be between 6 and 99"}), 400
      probability = calculate_bob_winning_probability(k)
      return jsonify({"res": probability})
    except ValueError:
      return jsonify({"error": "Invalid value for k"}), 400
  else:
    # Calculate probabilities for k = 6 through 99 and return the array
    probabilities = get_probability_list()
    return jsonify({"res": probabilities})

if __name__ == '__main__':
  app.run(debug=True)

