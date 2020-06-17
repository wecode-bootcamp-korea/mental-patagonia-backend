from django.shortcuts import render

import json
import bcrypt
import jwt
import requests

from patagonia.settings import SECRET_KEY, ALGORITHM
from member.models      import Member

from django.views       import View
from django.http        import JsonResponse, HttpResponse

class KakaoSignInCallbackView(View):
    def get(self, request):
        try:
            access_token = request.headers.get("Authorization", None)
            profile_request = requests.get(
                "https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"},
            )

            profile_json = profile_request.json()
            kakao_account = profile_json.get("kakao_account")
            email = kakao_account.get("email", None)
            kakao_id = profile_json.get("id")
            if Member.objects.filter(email = email).exists():
                member = Member.objects.get(email=email)
                token = jwt.encode({"email" : member.email}, SECRET_KEY, ALGORITHM)
                token = token.decode("utf-8")
                return JsonResponse({"token" : token ,"message" : "SUCCESS"}, status=200)
            else:
                firstname = kakao_account.get("profile", None).get("nickname", None)
                email = kakao_account.get("email", None)
                Member.objects.create(
                    email = email,
                    firstname = firstname[0],
                    lastname  = firstname[1:]
                )
            token = jwt.encode({"email" : email}, SECRET_KEY, ALGORITHM)
            token = token.decode("utf-8")

        except KeyError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

        except access_token.DoesNotExist:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

            return JsonResponse({"token" : token ,"message" : "SUCCESS"}, status = 200)

def login_decorator(func):

    def wrapper(self, request, *args, **kwargs):
        try:
            auth_token = request.headers.get('Authorization', None)
            payload    = jwt.decode(auth_token, SECRET_KEY, ALGORITHM)

            request.member = Member.objects.get(id=payload['member_id'])
            return func(self, request, *args, **kwargs)

        except Member.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=400)
        except jwt.exceptions.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=400)

    return wrapper
