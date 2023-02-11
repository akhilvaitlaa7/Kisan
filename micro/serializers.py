from rest_framework import serializers


class CalculationSerializer(serializers.Serializer):
    total_bags = serializers.IntegerField()
    weight_kgs = serializers.FloatField()
    commission = serializers.FloatField()
    labour_cost = serializers.IntegerField()
    price = serializers.FloatField()
