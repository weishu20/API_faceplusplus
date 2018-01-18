import requests

import json
from json import JSONDecoder
from common.key_secret import get_key,get_secret
from utils.base import isNull

def detect(filepath,return_landmark = 0,return_attributes="none"):
        if isNull(filepath):
                return
        http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"

        key = get_key()

        secret = get_secret()

        data = {"api_key": key,
                "api_secret": secret,
                "return_landmark":return_landmark,
                "return_attributes":return_attributes}

        files = {"image_file": open(filepath, "rb")}

        response = requests.post(http_url, data=data, files=files)

        req_con = response.content.decode('utf-8')

        req_dict = JSONDecoder().decode(req_con)

        print(req_dict)

        with open('result_json/detect_test_image.json', 'w') as json_file:
                json_file.write(json.dumps(req_dict, indent=2))
        return req_dict
