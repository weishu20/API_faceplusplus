import requests
import json
from json import JSONDecoder

from common.key_secret import get_key,get_secret
from utils.base import isNull,isNull_list

def create_faceSet(display_name="",outer_id="",tags="",face_tokens="",user_data="",force_merge=0):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "display_name":display_name,
            "outer_id": outer_id,
            "tags": tags,
            "face_tokens": face_tokens,
            "user_data": user_data,
            "force_merge": force_merge}
    if display_name == "":
        del data["display_name"]
    if outer_id == "":
        del data["outer_id"]
    if tags == "":
        del data["tags"]
    if face_tokens == "":
        del data["face_tokens"]
    if user_data == "":
        del data["user_data"]



    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/create_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def addFace_faceSet(faceset_token,face_tokens):
    if isNull(faceset_token) or isNull(face_tokens):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "faceset_token":faceset_token,
            "face_tokens": face_tokens}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/addFace_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def removeFace_faceSet(faceset_token,face_tokens):
    if isNull(faceset_token) or isNull(face_tokens):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "faceset_token":faceset_token,
            "face_tokens": face_tokens}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/removeFace_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def update_faceSet(faceset_token,new_outer_id):
    if isNull(faceset_token) or isNull(new_outer_id):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/update"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "faceset_token":faceset_token,
            "new_outer_id": new_outer_id}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/update_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def getDetail_faceSet(faceset_token,start=1):
    if isNull(faceset_token):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "faceset_token":faceset_token,
            "start": start}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/getDetail_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def delete_faceSet(faceset_token,check_empty=1):
    if isNull(faceset_token):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/delete"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "faceset_token":faceset_token,
            "check_empty": check_empty}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/delete_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def get_faceSet(tags="",start=1):
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "tags":tags,
            "start": start}
    if tags == "":
        del data["tags"]
    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/get_faceSet.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict