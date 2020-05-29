from django.shortcuts import render
# from django.models import
# from django.core import seralizers
# from django.contrib.auth import authenticate
# from django.http import HttpResponse

# from rest_framework.authtoken.models import Token
# from rest_framework.decoraters import api_view
# Create your views here.



def signup(request):
  email = request.data.get('email')
  password = request.data.get('password')
  # user = User.
