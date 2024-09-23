# Summary
# A function is a group of statements that together perform one task. The computer will not execute the code in a function unless you write code that calls the function.
# In this lesson, you learned how to call built-in functions, functions that are in a module, and functions (methods) that belong to an object.

# To call a built-in function, write code that follows this template:
# variable_name = function_name(arg1, arg2, … argN)
add_all_num = plusAll(a,b,c)

# To call a function from a module, import the module and write code that follows this template:
# import module_name
# variable_name = module_name.function_name(arg1, arg2, … argN)
# To call a method, write code that follows this template:
# variable_name = object_name.method_name(arg1, arg2, … argN)



# Assignment
# A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

# the number of manufactured items
# the number of items that the user will pack per box
# Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.