data = {
    "name": "NASA",
    "type": "County government",
    "id": "1",
    "email": "blasadsda"
}

allowed_fields = {
    "name": str,
    "id": int,
    "type":str
}
    
def verify_argument(data, fields):
    if not data and not fields:
        return False
    return True


def validate_keys(data, fields):
    return_value = verify_argument(data, fields)
    if return_value is False:
        return False
    for key, _ in fields.items():
        if  data.get(key) is None and not key in list(data.keys()) :
            return False
    return True

def validate_value_types(data, fields):
    return_value = verify_argument(data, fields)
    if return_value is False:
        return False
    for key, value in data.items():
        if type(value) == fields.get(key):
            return True
    return False

print(validate_keys(data, allowed_fields))
print(validate_value_types(data, allowed_fields))

