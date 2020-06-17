from django.urls import path

from .views import KakaoSignInCallbackView

urlpatterns = [
    path('/kakao', KakaoSignInCallbackView.as_view()),
]
