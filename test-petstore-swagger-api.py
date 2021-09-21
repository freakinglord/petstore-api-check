#!/usr/bin python3
import requests
import pytest
import json
from jsonschema import validate
from jsonschema import Draft6Validator

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",

    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "category": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                }
            },
            "name": {"type": "string"},
            "photoUrls": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"}
                    }
                }
            },
            "status": {"type": "string"}
        },
        "required": ["id", "name", "photoUrls", "tags", "status"]
    }
}

petstore_swagger_url = "https://petstore.swagger.io"
new_pet_id = 98789
new_pet_name = "test_new_pet"
api_key = "special_key"


def test_petstore_swagger():
    # make sure petstore swagger api is up
    response = requests.get(url=petstore_swagger_url)
    assert response.status_code == 200


def test_get_available_pets():
    # test to get all available pets
    url = petstore_swagger_url+"/v2/pet/findByStatus?status=available"
    response = requests.get(url=url)
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'
    resp_body = response.json()
    # try to validate response json schema that status is available
    validate(instance=resp_body, schema=schema)


def test_post_new_available_pet():
    # test to add new available pet
    url = petstore_swagger_url+"/v2/pet"
    data = {
        "id": new_pet_id,
        "category": {
            "id": new_pet_id,
            "name": new_pet_name
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": new_pet_id,
                "name": new_pet_name
            }
        ],
        "status": "available"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(response.text)
    new_pet = json.loads(response.text)
    print(new_pet["id"])
    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'

    # check if pet exist
    url = petstore_swagger_url+"/v2/pet/"+str(new_pet["id"])
    headers = {"accept": "application/json"}
    new_response = requests.get(url=url, headers=headers)
    print(new_response.text)


#@pytest.mark.skip()
def test_update_new_pet():
    # test to update new pet status to 'sold'
    url = petstore_swagger_url+"/v2/pet/"+str(new_pet_id)
    print(url)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = "name="+new_pet_name+"&status=sold"

    response = requests.post(url=url, data=data, headers=headers)
    assert response.status_code == 404
    url = petstore_swagger_url+"/v2/pet/"+str(9223372000001111497)
    response = requests.post(url=url, data=data, headers=headers)
    assert response.status_code == 200


#@pytest.mark.skip()
def test_delete_new_pet():
    url = petstore_swagger_url+"/v2/pet/"+str(new_pet_id)
    headers = {"api_key": api_key}
    response = requests.delete(url=url, headers=headers)
    assert response.status_code == 200



