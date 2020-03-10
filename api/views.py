from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, mixins, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Hotel
from .serializers import SignupSerializer, UserSerializer, ProfileSerializer, HotelSerializer

User = get_user_model()

# Create your views here.


class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ['post']


class LoginViewSet(viewsets.ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': user_serializer.data})


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def retrieve(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()
        if user:
            serializer = self.serializer_class(user)
        else:
            return Response("Details not found", status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class HotelViewset(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]

    queryset = Hotel.objects.all()
