from app.api.v1.models.party_models import parties
from app.api.v1.models.office_models import offices
def check_json(data):
    if not data:
        return False
    return True

class ValidateParty():
    def __init__(self, id, name, hqAddress, logoUrl):
        self.id = id
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    def check_id(self):
        if not isinstance(self.id, int):
            return False
        return True

    def check_name(self):
        if not isinstance(self.name, str)  or  (self.name==""):
            return False
        return True

    def check_hqaddress(self):
        if not isinstance(self.hqAddress, str) or (self.hqAddress == ""):
            return False
        return True

    def check_logoUrl(self):
        if not isinstance(self.logoUrl, str) or (self.logoUrl== ""):
            return False
        return True

    @classmethod
    def party_exists(cls, id):
        for party in parties:
            if party["id"] == id:
                return True
        return False

    @classmethod
    def get_party_by_id(cls, id):
        for party in parties:
            if party["id"] == id:
                return party
        return None


class ValidateOffice():
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type

    def check_office_id(self):
        if not isinstance(self.id, int):
            return False
        return True

    def check_office_name(self):
        if not isinstance(self.name, str) or (self.name == ""):
            return False
        return True

    def check_office_type(self):
        if not isinstance(self.type, str) or (self.type == ""):
            return False
        return True

    @classmethod
    def office_exists(cls, id):
        for office in  offices:
            if office["id"] == id:
                return True
        return False

    @classmethod
    def get_office_by_id(cls, id):
        for office in offices:
            if office["id"] == id:
                return office
        return None


    
