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
    def setUp(self): # 테스트를 하기 전에 실행  테스트에 필요한 db실행
        social = SocialLoginType.objects.create(name="Kakao")
        member1 = Member.objects.create(
            firstname="ko",
            lastname="daeyong",
            email="eodyd6564@naver.com",
            social_login_type=social
        )

    def tearDown(self): # 테스트가 끝나고 실행
        Member.objects.filter(firstname="ko").delete()

    @patch('member.views.requests')
    # member 앱의 views.py에서 사용될 requests를 patch
    def test_member_kakao_view_sign_up(self, mocked_request):
        client = Client()
        # 실제로 kakao API를 호출하지 않고
        # kakao API의 응답을 Fake로 작성
        class FakeResponse:
            def json(self):
                return {"kakao_account":{
                        "profile" : {
                            "nickname": "김솔이"
                        },
                    "email":"eodyd@naver.com"
                }}
        # test할 때, requests가 get 메서드로 받은 response는 FakeResponse의 instance
        mocked_request.get = MagicMock(return_value = FakeResponse())
        header = {'Authorization':'fake_token'}
        # Client의 get method에 header담기
        # **extra는 keyword arguments이나 header는 dict이므로 **을 붙여준다.
        response = self.client.get('/member/kakao', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 200)
