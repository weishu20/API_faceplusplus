import requests
from common.key_secret import get_key
from common.key_secret import get_secret
import json
from json import JSONDecoder
from utils.base import isNull

def compare_file(filepath1,filepath2,return_landmark = 0):
    if isNull(filepath1) or isNull(filepath2):
        return
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"

    key = get_key()

    secret = get_secret()



    data = {"api_key": key,
            "api_secret": secret,
            "return_landmark": return_landmark}

    files = {"image_file1":open(filepath1, "rb") ,
             "image_file2": open(filepath2, "rb")}

    response = requests.post(http_url, data=data, files=files)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/compare_file.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict

def compare_facetokens(face_token1,face_token2, return_landmark=0):
    if isNull(face_token1) or isNull(face_token2):
        return
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"

    key = get_key()

    secret = get_secret()


    data = {"api_key": key,
            "api_secret": secret,
            "return_landmark": return_landmark,
            "face_token1": face_token1,
            "face_token2": face_token2}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/compare_facetokens.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict