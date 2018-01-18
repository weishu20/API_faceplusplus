import requests
import json
from json import JSONDecoder

from common.key_secret import get_key,get_secret
from utils.base import isNull

def analyze_face(face_token,return_landmark = 0,return_attributes="none"):
    if isNull(face_token):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/face/analyze"

    key = get_key()

    secret = get_secret()



    data = {"api_key": key,
            "api_secret": secret,
            "face_token":face_token,
            "return_landmark": return_landmark,
            "return_attributes": return_attributes}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/analyze_face.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict


def getDetail_face(face_token):
    if isNull(face_token):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/face/getdetail"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "face_token": face_token}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/getDetail_face.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def setUserID_face(face_token,user_id):
    if isNull(face_token) or isNull(user_id):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/face/setuserid"

    key = get_key()

    secret = get_secret()

    data = {"api_key": key,
            "api_secret": secret,
            "face_token": face_token,
            "user_id": user_id}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/setUserID_face.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict
