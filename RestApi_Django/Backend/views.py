from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_users(request):
    users=User.objects.all()  #fetches from db
    serializer= UserSerializer(users, many=True)
    return Response(UserSerializer({'name': 'sten', 'age': 12}).data)

@api_view(['POST'])
def create_user(request):
    serialize= UserSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)