# test_read_dictionary.py
import unittest
from io import StringIO
from unittest.mock import patch
from studentsV2 import read_dictionary  # Replace 'your_module' with the actual module name

class TestReadDictionary(unittest.TestCase):
    try:
      x = 1
        # @patch('builtins.open', new_callable="")
        # def test_read_dictionary(self):
        #     """Test that the read_dictionary function correctly parses the CSV file."""
        #     expected_dict = {
        #         "123456789": "John Doe",
        #         "987654321": "Jane Smith"
        #     }
        #     result = read_dictionary("wk5/students.csv", 0)  # I-Number is the key (0th column)
        #     self.assertNotEqual(result, expected_dict)
            #    print("pass")
        
      AssertionError 
    except:
      print('An exception occurred')



if __name__ == '__main__':
    unittest.main()
