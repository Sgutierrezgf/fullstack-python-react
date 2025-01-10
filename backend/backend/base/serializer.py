# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'nombre', 'apellido', 'correo', 'telefono', 'genero', 'rol', 'estado']

# class AuthSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'gender', 'role', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Asegura que la contraseña no se lea al serializar
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Obtenemos la contraseña
        user = User.objects.create(**validated_data)  # Creamos el usuario
        user.set_password(password)  # Establecemos la contraseña de forma segura
        user.save()  # Guardamos el usuario
        return user