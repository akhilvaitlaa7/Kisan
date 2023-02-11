from rest_framework import generics
from rest_framework.response import Response

from micro.serializers import CalculationSerializer


class CalculationView(generics.GenericAPIView):
    serializer_class = CalculationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        total_bags = serializer.validated_data['total_bags']
        weight_kgs = serializer.validated_data['weight_kgs']
        commission = serializer.validated_data['commission']
        labour_cost = serializer.validated_data['labour_cost']
        price = serializer.validated_data['price']
        result = ((weight_kgs/100)*price - (total_bags*labour_cost))*(1-commission/100)
        return Response({"result": result})
