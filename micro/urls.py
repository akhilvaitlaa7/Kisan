from django.urls import path

from micro.views import CalculationCreateView,UserCreateView

urlpatterns = [
    path('calculate/', CalculationCreateView.as_view()),
    path('users/', UserCreateView.as_view()),
]
