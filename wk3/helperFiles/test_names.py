#Modified by John Russelle Domingo
#credits to BYU-IDAHO  source Code

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """ make_full_name("Sally", "Brown"), it would return "Brown; Sally"."""
    assert make_full_name("","") != 0
    assert make_full_name("A","B") == "B;A"
    assert make_full_name(" "," ") == " ; "
    assert make_full_name("Sally","Brown") == "Brown;Sally"
    assert make_full_name("John-Russelle","Domingo") == "Domingo;John-Russelle"
    assert isinstance(make_full_name("John-Russelle","Domingo"), str)


def test_extract_family_name():
    """extract_family_name("Brown; Sally"), it would return "Brown"."""
    assert extract_family_name != 0
    assert extract_family_name("A; B") == "A"
    assert extract_family_name(" ; ") == " "
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Domingo; John-Russelle") == "Domingo"
    assert isinstance(extract_family_name("Domingo; John-Russelle"), str)
 
def test_extract_given_name():
    assert extract_given_name != 0
    assert extract_given_name("A; B") == "B"
    assert extract_given_name(" ; ") == ""
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Domingo; John-Russelle") == "John-Russelle"
    assert isinstance(extract_given_name("Domingo; John-Russelle"), str)

    
    
 
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])  
# test_extract_given_name()