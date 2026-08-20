from django.urls import path
from .views import CreateUserView, VerifyAPIView, GetNewVerificationView

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerificationView.as_view()),
]