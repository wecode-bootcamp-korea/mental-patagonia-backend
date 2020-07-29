from django.shortcuts import render

import json
import bcrypt
import jwt
import requests

from patagonia.settings import SECRET_KEY, ALGORITHM
from member.models      import Member

from django.views       import View
from django.http        import JsonResponse, HttpResponse

class LoginConfirm:
    def __init__(self,original_function):
        self.original_function = original_function

    def __call__(self, request, *args, **kwargs):
        token = request.headers.get("Authorization", None)
        print(10)
        try:
            if token:
                print(20)
                token_payload	= jwt.decode(token, SECRET_KEY, ALGORITHM)
                user			= Member.objects.get(email=token_payload['email'])
                request.user	= user
                return self.original_function(self, request, *args, **kwargs)

            return JsonResponse({'message':'INVALID_USER'}, status=401)
        except jwt.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'}, status=401)

        except Member.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

class KakaoSignInCallbackView(View):
    def get(self, request):
        try:
            access_token = request.headers.get("Authorization", None)
            if type(access_token) == type(None):
                return JsonResponse({"message" : "ACCESS_DENIED"}, status = 401)

            profile_request = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},
            )
            print(profile_request.json())
            profile_json    = profile_request.json().get("kakao_account",None)
            print(profile_json)
            email           = profile_json.get("email", None)
            fullname        = profile_json.get("profile", None).get("nickname", None)

            if Member.objects.filter(email = email).exists():
                member = Member.objects.get(email=email)
                token = jwt.encode({"email" : member.email}, SECRET_KEY, ALGORITHM)
                token = token.decode("utf-8")
                return JsonResponse({"token" : token ,"message" : "SUCCESS"}, status=200)
            else:
                Member.objects.create(
                    email = email,
                    firstname = fullname[0],
                    lastname  = fullname[1:]
                )
            token = jwt.encode({"email" : email}, SECRET_KEY, ALGORITHM)
            token = token.decode("utf-8")

            return JsonResponse({"token" : token ,"message" : "SUCCESS"}, status = 200)

        except KeyError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

class MypageMainView(View):
    @LoginConfirm
    def get(self, request):
        try:
            member      = request.user
            address     = member.addressbook_set.filter(is_default=True)
            member_info = {
                "firstname" : member.firstname,
                "lastname"  : member.lastname,
                "email"     : member.email
            }
            if address:
                address_book = {
                    "name"          : address.name,
                    "firstname"     : address.firstname,
                    "lastname"      : address.lastname,
                    "address1"      : address.address1,
                    "address2"      : address.address2,
                    "city"          : address.city,
                    "zipcode"       : address.zipcode,
                    "phone_number"  : address.phone_number,
            }
            else:
                address_book = {}
            return JsonResponse({"member_info" : member_info, "address_book" : address_book}, status=200)
        except KeyError:
            return JsonResponse({"message" : "INVALID_KEY"}, status=400)

