from django.urls import path

from micro.views import CalculationView

urlpatterns = [
    path('calculate/', CalculationView.as_view(), name='calculate'),
]
