def main():
    # Open the provinces.txt file for reading
    with open('wk5\provinces.txt', 'r') as file:
        # Read the contents of the file into a list
        provinces_list = file.readlines()

    # Strip any extra whitespace or newline characters from each line
    provinces_list = [line.strip() for line in provinces_list]

    # Print the entire list
    print("Original List:", provinces_list)

    # Remove the first element from the list
    provinces_list.pop(0)

    # Remove the last element from the list
    provinces_list.pop()

    # Replace all occurrences of "AB" with "Alberta"
    provinces_list = ['Alberta' if province == 'AB' else province for province in provinces_list]

    # Count the number of elements that are "Alberta"
    alberta_count = provinces_list.count('Alberta')

    # Print the updated list and the count of "Alberta"
    print("Updated List:", provinces_list)
    print(f"Number of occurrences of 'Alberta': {alberta_count}")
    
    try
    
if __name__ == '__main__':
    main()    
    
    