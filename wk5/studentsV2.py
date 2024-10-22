# Author: John Russelle Domingo
# Date: Oct16_2024
import csv



def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            key = row[key_column_index]
            value = row[1]  # Assuming name is in the second column
            dictionary[key] = value
    
    return dictionary


def main():
    filename = "wk5/students.csv"
    student_dict = read_dictionary(filename, 0)  # Assuming I-Number is in the first column
    
    while True:
        # Get I-Number from the user
        i_number = input("Enter an I-Number (e.g., 123456789) or 'exit' to quit: ")
        
        if i_number.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        # Remove any dashes from the I-Number input
        i_number = i_number.replace('-', '')

        try:
            # Check if the I-Number is in the dictionary
            if i_number in student_dict:
                print(f"Student name: {student_dict[i_number]}")
            else:
                raise KeyError("No such student")  # Raise an exception if I-Number not found

        except KeyError as e:
            print(e)  # Print "No such student" if the I-Number is not in the dictionary

# Call main function
if __name__ == '__main__':
    main()