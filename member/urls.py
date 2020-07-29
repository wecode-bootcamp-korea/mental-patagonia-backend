from django.urls import path

from .views import KakaoSignInCallbackView, MypageMainView

urlpatterns = [
    path('/kakao', KakaoSignInCallbackView.as_view()),
    path('/', MypageMainView.as_view())
]
