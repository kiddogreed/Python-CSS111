def calculate_heart_rate_range(age):
  """Calculates the target heart rate range for strengthening the heart.

  Args:
    age: The person's age in years.

  Returns:
    A tuple containing the minimum and maximum heart rates.
  """

  max_heart_rate = 220 - age
  min_heart_rate = int(0.65 * max_heart_rate)
  max_heart_rate = int(0.85 * max_heart_rate)
  return min_heart_rate, max_heart_rate

def main():
  age = int(input("Enter your age: "))
  min_heart_rate, max_heart_rate = calculate_heart_rate_range(age)
  print(f"Your target heart rate range is {min_heart_rate}-{max_heart_rate} beats per minute.")

if __name__ == "__main__":
  main()