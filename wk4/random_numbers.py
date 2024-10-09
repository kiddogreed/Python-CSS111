import random

def append_random_numbers(num_list, count=1):
    """Appends 'count' random numbers default value =1 (whole or float) to the given list."""
    for _ in range(count):
        # Generate either a whole number or a float with one decimal place
        if random.choice([True, False]):
            num_list.append(random.randint(1, 100))  # Append whole number
        else:
            num_list.append(round(random.uniform(1, 100), 1))  # Append float with 1 decimal

def main():
    # Create an initial list of numbers
    numbers = [16.2, 75.1, 52.3] # Initial list
    
    #task
    print(numbers)
    
    # Append 1 random numbers (whole or float)
    append_random_numbers(numbers)
    print(numbers)
    # Append 5 random numbers (whole or float)
    append_random_numbers(numbers,5)
    print(numbers)
    # Print the updated list
    print("Updated List:", numbers)
    
#Stretch
def append_random_words(words_list, quantity=1):
    available_words = ["Apple", "Banana", "Calamansi", "Dragon Fruit", "Egg Plant", "Fruits", "Grape", "Honey Dew", "I", "Jack Fruit","Kiwi","Lemon"]
    for _ in range(quantity):
        words_list.append(random.choice(available_words))
   

# Call the main function to run the program
if __name__ == "__main__":
  main()
