import time
import numpy as np
import matplotlib.pyplot as plt
from functools import wraps

from dice_game import calculate_bob_winning_probability

def simple_time_stats(func):
  """
  A simplified decorator that calculates and reports the execution time of the decorated function.
  """
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute.")
    return result
  return wrapper


def plot_probability_chart(func):
  """
  A decorator that plots the function's returned k values and their corresponding probabilities.
  """
  @wraps(func)
  def wrapper(*args, **kwargs):
    k_values, probabilities = func(*args, **kwargs)

    # Plotting logic
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, probabilities, marker='o', linestyle='-', color='b')
    plt.title('Bob\'s Winning Probability for Different k Values')
    plt.xlabel('k Value')
    plt.ylabel('Winning Probability')
    plt.grid(True)
    plt.show()
    
    return k_values, probabilities
  return wrapper


@simple_time_stats
def time_list_calc():
  k_values = np.arange(6, 100)  # Generate k values
  probabilities = calculate_bob_winning_probability(k_values)  # Compute probabilities
  return k_values, probabilities 


@plot_probability_chart
def get_probability_data():
  return time_list_calc()


if __name__ == '__main__':
  get_probability_data()
