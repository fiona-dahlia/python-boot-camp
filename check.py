import json

json_response = """{
    "active": true,
    "scope": "offline_access",
    "username": "k.appadurai@spglobal.com",
    "exp": 1654202377,
    "iat": 1654198777,
    "sub": "k.appadurai@spglobal.com",
    "aud": "api://default",
    "iss": "https://dev-15107069.okta.com/oauth2/default",
    "jti": "AT.kFKj0Qc6EI8Je2kmeL0XLRCrFgwgLVwMuNPg11aiUjc.oarhtbbj5Q222pC1w5d6",
    "token_type": "Bearer",
    "client_id": "0oa55mqxt5yUbo1t75d7",
    "uid": "00u3mk9sy6fvIlRfh5d7"
}"""

response = json.loads(json_response)
print(response)

if response.get('active'):
    print('Valid token')
else:
    print('Invalid token')
