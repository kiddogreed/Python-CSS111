W03 Prepare: Testing Functions


Inefficient Testing
During previous lessons, you tested your programs by running them, typing user input, reading the program’s output, and verifying that the output was correct. This is a valid way to test a program. However, it is time consuming, tedious, and error prone. A much better way to test a program is to test its functions individually and to write separate test functions that automatically verify that the program’s functions are correct.

In this course, you will write test functions in a Python file that is separate from your Python program. In other words, you will keep normal program code and test code in separate files.

install pytest using pip install pytest



How to Test a Function
To test a function you should do the following:

Write a function that is part of your normal Python program.
Think about different parameter values that will cause the computer to execute all the code in your function and will possibly cause your function to fail or return an incorrect result.
In a separate Python file, write a test function that calls your program function and uses an assert statement to automatically verify that the value returned from your program function is correct.
Use pytest to run the test function.
Read the output of pytest and use that output to help you find and fix mistakes in both your program function and test function.


# 👇️ In a virtual environment or using Python 2
pip install pytest

# 👇️ For Python 3 (could also be pip3.10 depending on your version)
pip3 install pytest

# 👇️ If you get a permissions error
sudo pip3 install pytest
pip install pytest --user

# 👇️ If you don't have pip in your PATH environment variable
python -m pip install pytest

# 👇️ For Python 3 (could also be pip3.10 depending on your version)
python3 -m pip install pytest

# 👇️ Using py alias (Windows)
py -m pip install pytest

# 👇️ For Anaconda
conda install -c anaconda pytest