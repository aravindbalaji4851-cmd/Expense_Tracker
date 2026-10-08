
from django.urls import path

from spending.views import SignUpView,GetMeView

urlpatterns = [

    path('register/',SignUpView.as_view()),
    path('getme/',GetMeView.as_view()),
]
