import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '975cddad6e5d7e9f2b12bcfb25504a79'
redirect_uri = 'https://example.com/oauth'
code = 'N200NgYVOqInwOTP2Tm0SvrjMQJkzIk2FuvTcL6zKvHcCHVxvrWGDKwnzjvyXwyl2LLwyQopdSkAAAGBmH6ueA'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': code,
}

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)
print(tokens)
