from flask import jsonify, request
from flask import Blueprint
from app.api.v1.models.party_models import Party, parties
from app.api.v1.models.office_models import Office, offices
from app.api.v1.utils import ValidateOffice, ValidateParty, check_json

api = Blueprint('api', __name__)


@api.route('/parties', methods=['GET'])
def get_all_parties():
    data = []
    for party in parties:
        temp_party = {
            "id": party["id"],
            "name": party["name"],
            "hqAddress": party["hqAddress"],
            "logoUrl": party["logoUrl"]
        }
        data.append(temp_party)
    return jsonify({
        "status": 200,
        "data": data
    }), 200


@api.route('/parties', methods=['POST'])
def create_a_party():
    data = request.get_json(force=True)
    party = ValidateParty(data.get('id'), data.get('name'), data.get("hqAddress"), data.get("logoUrl"))
    if check_json(data) and party.check_name() and party.check_id() and party.check_hqaddress() and party.check_logoUrl() and  not(ValidateParty.party_exists(party.id)):
        new_party = Party.create_party(party.id, party.name, party.hqAddress, party.logoUrl)
        return jsonify({
            "status": 201,
            "data": [{
                "id": new_party["id"],
                "name": new_party["name"]
            }]
        }), 201
    return jsonify({
        "status": 400,
        "data": [{
            "message": "Error please check the data you are trying to submit"
        }]
    }), 400

    

@api.route('/parties/<int:party_id>', methods=['GET'])
def get_a_party(party_id):
        for party in parties:
            if party['id'] == party_id:
                return jsonify(party), 200
        return jsonify({"message": "party do not exists"}), 404


@api.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_a_party(party_id):
    party = ValidateParty.get_party_by_id(party_id)
    if  party:
        party_index = parties.index(party)
        del(parties[party_index])
        return jsonify({
            "status": 200,
            "data": [
                {
                    "message": "party deleted successfully"
                }
            ]
        }), 200
    return jsonify({
        "message": "party does not exists"
    })
        


@api.route('/parties/<int:party_id>/name', methods=['PATCH'])
def edit_a_party(party_id):
    data = request.get_json()
    if check_json(data) and data.get("name") is not None:
        party_to_edit = ValidateParty.get_party_by_id(party_id)
        if party_to_edit:
            party_to_edit['name'] = data['name']
            return jsonify({
                    "status": 200,
                    "data": [
                        {
                            "id": party_to_edit['id'],
                            "name": party_to_edit['name']
                        }
                    ]
                })
    return jsonify({"message": "Party does not exists"}), 404
   


@api.route('/offices', methods=['GET'])
def get_all_offices():
    data = []
    for office in offices:
        temp_office = {
            "id": office["id"],
            "type": office["type"],
            "name": office["name"]
        }
        data.append(temp_office)
    return jsonify({
        "status": 200,
        "data": data
    }), 200


@api.route('/offices', methods=['POST'])
# def create_an_office():
#     data = request.get_json(force=True)
#     allowed_fields = {
#         "id": int,
#         "name": str,
#         "type": str,
#     }
#     keys_validation_response = validate_keys(data, allowed_fields)
#     valuetypes_validation_response = validate_keys(data, allowed_fields)
#     if next(filter(lambda x: x['id'] == data['id'], offices), None):
#         return jsonify({"message": "Office with that id already exists", "code": 400}), 400
#     if keys_validation_response and valuetypes_validation_response:
#         new_office = Office.create_office(data['id'], data['type'], data['name'])
#         return jsonify({
#             "status": 201,
#             "data": [{
#                 "id": new_office["id"],
#                 "type": new_office["type"],
#                 "name": new_office["name"]
#             }]
#         }), 201


@api.route('/offices/<int:office_id>', methods=['GET'])
def get_an_office(office_id):
        for office in offices:
            if office["id"] == office_id:
                return jsonify({
                    "status": 200,
                    "data": [{
                        "id": office["id"],
                        "type": office["type"],
                        "name": office["name"]
                    }]
                }), 200
        return jsonify({
            "status": 404,
            "data": [{
                "message": "Office do not exists"
            }]
        })
