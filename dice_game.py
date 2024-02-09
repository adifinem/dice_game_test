#!/usr/bin/env python3
import numpy as np

# Task outline: Given two players, Bob and Alice, that take turns in rolling a fair k-sided die. Whoever
# rolls a k first wins the game. The Python program should output the probability that Bob wins the game
# for k = 6 thru 99. That is, the output will be an array of probabilities where index 0 is the probability
# when k = 6; index 1 when k = 7; etc.

# Implementation notes:
# Probability is calculated using the geometric series formula to avoid hitting max recursion depth or potential
# halting problems, since the game has no finite non-win termination point (and it's just nice and sipmle).
# Complexity scales linearaly as O(n) where n=len(k_values), so remains in polynomial time. 
# Calculations are vectorized using numpy for better performance. Decimal may be useful if we want very
# high resolution floats at some point (pun possibly intended).

def calculate_bob_winning_probability(k_values):
    # Convert k_values to a numpy array for vectorized operations
    k = np.array(k_values)
    # Vectorized computation of not rolling a k for one turn
    not_k_probability = (k - 1) / k
    # Vectorized computation of Bob's winning probability using the formula for the sum of a geometric series
    bob_winning_probability = (1/k) / (1 - not_k_probability**2)
    return bob_winning_probability


def get_probability_list():
    # Generate a range of k values using numpy for better handling of larger numbers
    k_values = np.arange(6, 100)  # This creates an array of k values starting from 6 to 99
    probabilities = calculate_bob_winning_probability(k_values)
    return probabilities.tolist()  # Convert the numpy array back to a list if needed


if __name__ == '__main__':
  print(get_probability_list())

