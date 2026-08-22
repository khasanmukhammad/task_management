from django.urls import path
from .views import CreateUserView, VerifyAPIView, GetNewVerificationView, ChangeUserInformationView, \
    LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerificationView.as_view()),
    path('change-user/', ChangeUserInformationView.as_view()),
]