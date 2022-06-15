import re

def validate_requested_amount(amount):
    if re.findall('^[0-9]$|^[1-9][0-9]$|^[1-9][1-9][0-9]$|^(1000)$',amount):
        return True
    else:
        return False

def validate_description_length(length):
    if len(length) <= 100:
        return True
    else:
        return False
