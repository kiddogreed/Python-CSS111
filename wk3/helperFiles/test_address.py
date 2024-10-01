#Modified by John Russelle Domingo
#credits to BYU-IDAHO  source Code

from address import extract_city, \
    extract_state, extract_zipcode
import pytest

# in this form: number street, city, state zipcode
# For example: 525 S Center St, Rexburg, ID 83460

def test_extract_city():
    assert extract_city != 0
    assert extract_city(", ,") == ""
    assert extract_city("525 S Center St, Rexburg, ID 83460")== "Rexburg"
    assert isinstance(extract_city("525 S Center St, Rexburg, ID 83460"), str)

def test_extract_state():
    assert extract_state != 0
    assert extract_city(" , , ") == ""
    assert extract_state("525 S Center St, Rexburg, ID 83460")== "ID"
    assert isinstance(extract_state("525 S Center St, Rexburg, ID 83460"), str)
   
def test_extract_zipcode():
    assert extract_zipcode != 0
    assert extract_city(", ,") == ""
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460")== "83460"
    assert isinstance(extract_zipcode("525 S Center St, Rexburg, ID 83460"), str)
    
    
    
 
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])  
# test_extract_given_name()