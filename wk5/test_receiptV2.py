# Author: John Russelle Domingo
# Date: OCT22_2024
# Desc: Test script for receiptV2.py using unittest to check basic functionality.

import unittest
from receiptV2 import read_dictionary, main
from io import StringIO
import sys

class TestReceiptV2(unittest.TestCase):
    
    def test_read_dictionary(self):
        # Test reading a valid products CSV file.
        filename = "wk5\\products.csv"
        result = read_dictionary(filename, 0)
        
        # Assert that the dictionary is not empty
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        
        # Assert that certain expected keys are in the dictionary
        self.assertIn('D150', result)
        self.assertIn('D083', result)
        
        # Assert that the values are lists with expected content
        self.assertIsInstance(result['D150'], list)
        self.assertEqual(result['D083'][1], '1 cup yogurt')  # Replace with actual name in your products.csv
    
    
    def test_main_function_output(self):
        # Test the output of the main function (without real file reading)
        # Capture the printed output of the main function
        captured_output = StringIO()          # Create StringIO object
        sys.stdout = captured_output          # Redirect stdout
        
        try:
            main()                            # Run the main function
        except SystemExit:
            pass  # Ignore exit calls for test
        
        sys.stdout = sys.__stdout__           # Reset redirect
        output = captured_output.getvalue()   # Get output
        
        # Assert that certain key output strings are present
        self.assertIn("Russelle's Corner Store", output)
        self.assertIn("Requested Items", output)
        self.assertIn("Number of items:", output)
        self.assertIn("Subtotal:", output)
        self.assertIn("Sales Tax (6%):", output)
        self.assertIn("Total:", output)
        self.assertIn("Thank you for shopping", output)


  

if __name__ == '__main__':
    unittest.main()
