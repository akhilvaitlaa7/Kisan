from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from micro.models import Calculation,User
from micro.serializers import CalculationSerializer,UserSerializer


class CalculationCreateView(generics.ListCreateAPIView):
    queryset = Calculation.objects.all()
    serializer_class = CalculationSerializer

    def perform_create(self, serializer):
        user_id = self.request.data['user']
        user = User.objects.get(id=user_id)
        total_bags = self.request.data['total_bags']
        weight_kgs = self.request.data['weight_kgs']
        commission = self.request.data['commission']
        labour_cost = self.request.data['labour_cost']
        price = self.request.data['price']
        result = ((weight_kgs/100)*price - (total_bags*labour_cost))*(1-commission/100)
        serializer.save(result=result, user=user)
        return Response(result)

    def get_queryset(self):
        user = self.request.data.get('user')
        queryset = Calculation.objects.all()
        if user:
            queryset = queryset.filter(user=user)
        return queryset


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        name = self.request.data['name']
        serializer.save(name=name)
        return Response({'status': 'User Created'})