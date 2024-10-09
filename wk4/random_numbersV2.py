import random

# Function to append random numbers to a list
def append_random_numbers(numbers_list, quantity):
    for _ in range(quantity):
        if random.choice([True, False]):  # Randomly choose between float or integer
            numbers_list.append(round(random.uniform(0, 100), 1))  # Append a float with 1 decimal
        else:
            numbers_list.append(random.randint(0, 100))  # Append a whole number

# Function to append random words to a list
def append_random_words(words_list, quantity=1):
    available_words = ["apple", "banana", "grape", "orange", "kiwi", "mango", "pear", "cherry", "peach", "plum"]
    for _ in range(quantity):
        words_list.append(random.choice(available_words))

# Main function to drive the program
def main():
    # Create initial list of numbers
    numbers_list = [random.randint(0, 100) for _ in range(5)]
    print(f"Initial numbers list: {numbers_list}")
    
    # Ask user how many random numbers to append
    num_to_append = int(input("How many random numbers do you want to append? "))
    append_random_numbers(numbers_list, num_to_append)
    print(f"Updated numbers list: {numbers_list}")
    
    # Create initial list of words
    words_list = ["start", "finish", "begin", "end"]
    print(f"\nInitial words list: {words_list}")
    
    # Ask user how many random words to append
    words_to_append = int(input("How many random words do you want to append? "))
    append_random_words(words_list, words_to_append)
    print(f"Updated words list: {words_list}")
    
    # Fun addition: printing a final message
    print("\nThanks for using this randomizer! Hope it was fun!")

# Run the main function
if __name__ == "__main__":
    main()
