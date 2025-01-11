from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated



class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is None:
            return Response({'detail': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.is_active:
            return Response({'detail': 'Usuario inactivo'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'role': user.role,
            }
        })

class IsAdmin(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso solo a administradores.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin'


class IsUserOrAdmin(permissions.BasePermission):
    """
    Permiso personalizado para permitir acceso a usuarios o administradores.
    """

    def has_permission(self, request, view):
        return request.user and (request.user.role == 'admin' or request.user.role == 'user')



class UserListView(APIView):
    # permission_classes = [IsAuthenticated, IsAdmin]
    permission_classes = [permissions.AllowAny] # Asegúrate de que esto esté configurado

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class EditUserView(APIView):
    # permission_classes = [IsAuthenticated, IsAdmin]
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if user.role == 'admin' and user == request.user:
                return Response({'detail': 'Un administrador no puede editarse a sí mismo'}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeactivateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        if user.role == 'admin' and user == request.user:
            return Response({'detail': 'Un administrador no puede desactivarse a sí mismo'}, status=status.HTTP_403_FORBIDDEN)
        user.is_active = False
        user.save()
        return Response({'detail': 'Usuario desactivado correctamente'}, status=status.HTTP_200_OK)

class ActivateUserView(APIView):  # Nueva vista para activar
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        if user.role == 'admin' and user == request.user:
            return Response({'detail': 'Un administrador no puede activarse a sí mismo'}, status=status.HTTP_403_FORBIDDEN)
        user.is_active = True
        user.save()
        return Response({'detail': 'Usuario activado correctamente'}, status=status.HTTP_200_OK)



