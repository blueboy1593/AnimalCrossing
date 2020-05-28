from rest_framework import serializers
from .models import Fish, Insect, Fossil, Painting, Animal
# from accounts.serializers import UserSerializer
# from accounts.models import User

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ['id', 'name', 'month', 'time', 'size', 'location', 'price']


class InsectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insect
        fields = ['id', 'name', 'month', 'time', 'location', 'price']


class FossilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fossil
        fields = ['id', 'name', 'price']


class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['id', 'name', 'real', 'engname', 'memo' ]


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'engname', 'gender', 'birthday', 'personality', 'sort']


