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


# Call main to start this program.
if __name__ == "__main__":
    First()
    main()