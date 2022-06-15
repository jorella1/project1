from service.validate_service import *
import pytest

@pytest.mark.parametrize("amount, expected",(
    ('0',True),('cat',False),('-5',False),('5',True),('5000',False),('1000',True),
    ('999',True),('1',True),('fsdf sdfs',False),('123',True),('-10000',False),('014123412=1412095$^*2342',False)
    )) 

def test_validate_requested_amount(amount,expected):
    assert validate_requested_amount(amount) == expected

@pytest.mark.parametrize("length, expected",(
    ('sfsdfsdfjlkakda   ergdrgdfgsdfgagdagadgadfgdafgdagadfgdafvdafgdafgsergregeargeargera',True),
    ('sdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff',False),
    ('my feet hurt because this company doesnt pay enough to let my buy good work boots', True),
    ('This wouldnt stop talking and i yelled him now im on probation and you guys wont give me paid leave and its unfair because that guy was really annoying and everyone was complaining but nobody wanted to tell him to stop talking so i had to say something. I was just trying to be the good guy in the situation.',False)
))
def test_validate_description_length(length,expected):
    assert validate_description_length(length) == expected