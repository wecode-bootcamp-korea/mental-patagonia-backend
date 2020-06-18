from django.test import TestCase

import jwt
import json
import unittest

from django.test        import TransactionTestCase, Client
from patagonia.settings import SECRET_KEY
from unittest.mock      import patch, MagicMock
from .models            import Member, SocialLoginType
from .views             import KakaoSignInCallbackView

client = Client()
class KakaoLoginTest(TransactionTestCase):
    def setUp(self):
        social = SocialLoginType.objects.create(name="Kakao")
        member1 = Member.objects.create(
            firstname="ko",
            lastname="daeyong",
            email="eodyd6564@naver.com",
            social_login_type=social
        )

    def tearDown(self):
        Member.objects.filter(firstname="ko").delete()

    @patch('member.views.requests')
    def test_member_kakao_view_sign_up(self, mocked_request):
        client = Client()
        class FakeResponse:
            def json(self):
                return {"kakao_account":{
                        "profile" : {
                            "nickname": "김솔이"
                        },
                    "email":"eodyd@naver.com"
                }}
        mocked_request.get = MagicMock(return_value = FakeResponse())
        header = {'Authorization':'fake_token'}
        response = self.client.get('/member/kakao', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 200)
