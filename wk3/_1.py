import math
import pytest
# def deposit(amount):
#   # In order for this program to work correctly and
#   # for the bank records to be correct, we must not
#   # allow someone to deposit a zero or negative amount.
#   assert amount > 0


# from pytest import pytest

#def approx(expected_value, rel=None, abs=None, nan_ok=False):
    
print(pytest.__version__)
temperature = -1
given_name = "Temperature"
balance = 1
school_year = 21
assert temperature < 0
assert len(given_name) > 0
assert balance == 1
assert school_year != "senior"
print("no error")

def test_min():
  assert min(7, -3, 0, 2) == -3
  print("no error")
  
# Example 4
# The variables e and f can be any floating-
# point numbers from any calculation.
e = 7.135
f = 7.128
if abs(e - f) < 0.01:
    print(f"{e} and {f} are close enough so")
    print("we'll consider them to be equal.")
else:
    print(f"{e} and {f} are not close and")
    print("therefor not equal.")


#def approx(expected_value, rel=None, abs=None, nan_ok=False)

def test_function(actual_value,expected_value):
  assert actual_value == pytest.approx(expected_value)
  return(f"no error in this function actual_value:{actual_value} is equal to expected_value:{expected_value}")
print(test_function(1123,1123) ) 
    
#Example 5
def test_sqrt(val):
  assert math.sqrt(5) == pytest.approx(2.24, rel=0.01)
  print(f"no error in this function actual_value:{val} is equal to expected_value:{pytest.approx(2.24, rel=0.01)}")
test_sqrt(5)

# Example 6
# Compute the tolerance.
tolerance = expected_value * rel
# Use the tolerance to determine if the actual
# and expected values are close enough to be
# considered equal.


if abs(actual_value - expected_value) < tolerance:
    return True
else:
    return False
# # weather.py
# def cels_from_fahr(fahr):
#   """Convert a temperature in Fahrenheit to
#   Celsius and return the Celsius temperature.
#   """
#   cels = (fahr - 32) * 5 / 9
#   return cels


# test_weather.py
# from weather import cels_from_fahr
# from pytest import approx
# import pytest
# def test_cels_from_fahr():
#     """Test the cels_from_fahr function by calling it and
#     comparing the values it returns to the expected values.
#     Notice this test function uses pytest.approx to compare
#     floating-point numbers.
#     """
#     assert cels_from_fahr(-25) == approx(-31.66667)
#     assert cels_from_fahr(0) == approx(-17.77778)
#     assert cels_from_fahr(32) == approx(0)
#     assert cels_from_fahr(70) == approx(21.1111)
# # Call the main function that is part of pytest so that the
# # computer will execute the test functions in this file.
# pytest.main(["-v", "--tb=line", "-rN", __file__])
