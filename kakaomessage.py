import json
import requests


# XXX 출처: https://gam860720.tistory.com/522 [땡감:티스토리]
#  get token -> get_kakaotoken.py

#발행한 토큰 불러오기
with open("token.json","r") as kakao:
    tokens = json.load(kakao)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

txt = 'line1\nline2'
data = {
       'object_type': 'text',
       'text': txt,
       'link': {
           'web_url': 'https://developers.kakao.com',
           'mobile_web_url': 'https://developers.kakao.com'
       },
       'button_title': '키워드'
   }
   
# https://example.com/oauth
   
data = {'template_object': json.dumps(data)}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

