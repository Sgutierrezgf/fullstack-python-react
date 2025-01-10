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
        
        # Usamos authenticate para validar las credenciales
        user = authenticate(email=email, password=password)
        
        if user is None:
            return Response({'detail': 'Usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not user.is_active:
            return Response({'detail': 'Usuario inactivo'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Si la autenticación fue exitosa, generamos el token JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
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
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class EditUserView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

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
    permission_classes = [IsAuthenticated, IsAdmin]

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        if user.role == 'admin' and user == request.user:
            return Response({'detail': 'Un administrador no puede desactivarse a sí mismo'}, status=status.HTTP_403_FORBIDDEN)
        user.is_active = False
        user.save()
        return Response({'detail': 'Usuario desactivado correctamente'}, status=status.HTTP_200_OK)




































































# from django.contrib.auth import authenticate
# from rest_framework import status
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# import jwt
# from datetime import datetime, timedelta
# from .models import User
# from .serializer import UserSerializer, AuthSerializer
# from django.conf import settings
# from .authentication import CookieJWTAuthentication
# from .permissions import IsAdmin

# # Clave secreta para JWT
# SECRET_KEY = settings.SECRET_KEY

# # Registro de nuevo usuario
# class RegisterUserView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             # Obtener la contraseña del cuerpo de la solicitud
#             password = request.data.get('password')
#             user = serializer.save()
#             # Cifrar la contraseña antes de guardarla
#             user.set_password(password)
#             user.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Autenticación de usuario (login)
# class AuthUserView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # Autenticación
#         user = authenticate(username=username, password=password)

#         # Verifica que el usuario exista y la contraseña sea correcta
#         if user is None:
#             return Response({"detail": "Usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)

#         if user.estado == 'inactivo':
#             return Response({"detail": "Usuario inactivo"}, status=status.HTTP_400_BAD_REQUEST)

#         # Genera un token JWT
#         token = jwt.encode(
#             {
#                 'user_id': user.id,
#                 'rol': user.rol,  # Incluye el rol en el payload del token
#                 'exp': datetime.utcnow() + timedelta(days=7),  # Expiración de 7 días
#             },
#             settings.SECRET_KEY,
#             algorithm='HS256'
#         )

#         # Devuelve el token JWT
#         return Response({'token': token}, status=status.HTTP_200_OK)
    
    
# # Listar usuarios (solo administradores)
# class ListUsersView(APIView):
#     permission_classes = [AllowAny]  

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# # Editar usuario (solo administradores)
# class EditUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, pk):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Desactivar usuario (solo administradores)
# class DeactivateUserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def put(self, request, pk):
#         user = User.objects.get(pk=pk)
#         if user.rol == 'admin' and user.id == request.user.id:
#             return Response({"detail": "No puedes desactivar a ti mismo"}, status=status.HTTP_400_BAD_REQUEST)
        
#         user.estado = 'inactivo'
#         user.save()
#         return Response({"detail": "Usuario desactivado"})

