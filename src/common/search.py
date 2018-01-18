import requests
from common.key_secret import get_key
from common.key_secret import get_secret
import json
from json import JSONDecoder
from utils.base import isNull

def search(face_token,faceset_token,return_result_count = 1):
    if isNull(face_token) or isNull(faceset_token):
        return
    http_url ="https://api-cn.faceplusplus.com/facepp/v3/search"

    key = get_key()

    secret = get_secret()



    data = {"api_key": key,
            "api_secret": secret,
            "face_token": face_token,
            "faceset_token": faceset_token,
            "return_result_count": return_result_count}

    response = requests.post(http_url, data=data)

    req_con = response.content.decode('utf-8')

    req_dict = JSONDecoder().decode(req_con)

    print(req_dict)

    with open('result_json/research.json', 'w') as json_file:
        json_file.write(json.dumps(req_dict, indent=2))
    return req_dict
