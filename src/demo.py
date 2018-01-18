from common.face import analyze_face,getDetail_face,setUserID_face
from common.faceSet import create_faceSet,addFace_faceSet,removeFace_faceSet,update_faceSet,getDetail_faceSet,delete_faceSet,get_faceSet
from common.detect import detect
from common.compare import compare_file,compare_facetokens
from common.search import search


user_id = "whatever_user_id"
return_attributes="gender,age,smiling,emotion"
face_tokens = []
new_outer_id = "whatever_outer_id"
return_attributes1="gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze,skinstatus"
return_landmark= 2
filepath="../images/test_image.jpg"
filepath1 ="../images/our_data/test_other/1.jpg"
filepath2 ="../images/our_data/test_other/3.jpg"





# req_dict = detect(filepath,return_landmark,return_attributes)
#
# faces = req_dict['faces']
#
# for face in faces:
#     face_tokens.append(face['face_token'])
# print(face_tokens)
face_tokens = ['a447dcc5d88dbea8d7d19f35214ad23d', '523ce899c798eababdc8528b4cec87c6', '3016a8900306fa3e218b29758f10495f', '65b7afac02190153f8360a3054777b41', '25692fba067fec9c0a90c4ab96c1fc6c']


face_token = face_tokens[0]
face_token_str = ','.join(face_tokens[:4])
# face_token1 = face_tokens[1]
#
# compare_file(filepath1,filepath2,return_landmark = 0)
# compare_facetokens(face_token,face_token1, return_landmark=0)
#
#
# getDetail_face(face_token)
# setUserID_face(face_token,user_id)
# getDetail_face(face_token)
# analyze_face(face_token, return_landmark, return_attributes1)

# faceSet_req = create_faceSet(display_name="",outer_id="",tags="",face_tokens="",user_data="",force_merge=0)
# faceset_token = faceSet_req['faceset_token']

faceset_token = 'df9b303202eb5e61579667d1feb0855f'
#addFace_faceSet(faceset_token, face_token_str)
# # getDetail_faceSet(faceset_token, start=1)
# # removeFace_faceSet(faceset_token, face_token)
# # update_faceSet(faceset_token, new_outer_id)
# # getDetail_faceSet(faceset_token, start=1)
# # get_faceSet(tags="", start=1)
#
search(face_token, faceset_token, return_result_count=4)
# delete_faceSet(faceset_token, check_empty=1)








