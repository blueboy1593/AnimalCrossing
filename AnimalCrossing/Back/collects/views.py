from django.shortcuts import render, get_object_or_404
# import openpyxl
from .models import Fish, Insect, Animal, Painting, Fossil
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import FishSerializer, InsectSerializer, FossilSerializer, AnimalSerializer, PaintingSerializer
# from accounts.models import User
from rest_framework.permissions import AllowAny 
from rest_framework import serializers


@api_view(['GET'])
@permission_classes([AllowAny])
def fishes(request):
    fishes = Fish.objects.all()
    serializer = FishSerializer(fishes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def insects(request):
    insects = Insect.objects.all()
    serializer = InsectSerializer(insects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def fossils(request):
    fossils = Fossil.objects.all()
    serializer = FossilSerializer(fossils, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def paintings(request):
    paintings = Painting.objects.all()
    serializer = PaintingSerializer(paintings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def animals(request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)

