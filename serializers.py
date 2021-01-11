from rest_framework import serializers
from .models import MainMenu
from get_from_app.serializers import MyModel1Serializer, MyModel2Serializer

from get_from_app.models import MyModel1

from get_from_app.models import MyModel2


class ModelMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMain
        fields = '__all__'


class FiltersSerializers(serializers.Serializer):
    model_main = ModelMainSerializer(read_only=True, many=True)
    model_1 = Model1Serializer(read_only=True, many=True)
    model_2 = Model2Serializer(read_only=True, many=True)
