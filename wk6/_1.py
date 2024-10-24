#Author John Russelle Domingo
#Date: OCT24_2024


#types of programming
#PRoceedural
# Example 1
def First():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")


#Delarative
#SQL
# -- Example 2
# SELECT AVG(numbers) FROM table;

#Functional
# Example 3
from functools import reduce
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.




#OOP
# Example 5
def mainx():
    # Create an empty list that will hold fabric names.
    fabrics = []
    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")
    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)
    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")
    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"
    print(fabrics)
    # Remove the last element from the fabrics list.
    fabrics.pop()
    # Remove denim from the fabrics list.
    fabrics.remove("denim")
    print(fabrics)
# Call main to start this program.

# Call main to start this program.
if __name__ == "__main__":
    First()
    main()
    mainx()  # Call mainx to start this program.