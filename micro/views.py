from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User

from micro.models import Calculation, User, ImageModel
from micro.serializers import CalculationSerializer, UserSerializer, UserImageSerializer


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
        result = ((weight_kgs / 100) * price - (total_bags * labour_cost)) * (1 - commission / 100)
        serializer.save(result=result, user=user)
        return Response(result)

    def get_queryset(self):
        user = self.request.data.get('user')
        queryset = Calculation.objects.all().order_by('-timestamp')
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


class UserImageCreateView(generics.ListCreateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = UserImageSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_authenticated:
            # Get the default user, for example with id=1
            user = User.objects.get(id=1)
        image = self.request.data['image']
        serializer.save(user=user, image=image)

    def get_queryset(self):
        user = self.request.data.get('user')
        queryset = ImageModel.objects.all().order_by('-timestamp')
        if user:
            queryset = queryset.filter(user=user)
        return queryset
