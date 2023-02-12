from rest_framework import serializers

from micro.models import Calculation, User


class CalculationSerializer(serializers.Serializer):
    total_bags = serializers.IntegerField()
    weight_kgs = serializers.FloatField()
    commission = serializers.FloatField()
    labour_cost = serializers.IntegerField()
    price = serializers.FloatField()
    result = serializers.FloatField(required=False)

    def create(self, validated_data):
        return Calculation.objects.create(**validated_data)

    def to_representation(self, instance):
        if self.context['request'].method == 'GET':
            return super().to_representation(instance)
        else:
            return {'result': instance.result}



class UserSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

