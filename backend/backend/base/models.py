# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, username, password, **extra_fields):
#         if not username:
#             raise ValueError("El usuario debe tener un nombre de usuario")
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('rol', 'admin')
#         return self.create_user(username, password, **extra_fields)

# class User(AbstractBaseUser):
#     GENDER_CHOICES = [
#         ('M', 'Masculino'),
#         ('F', 'Femenino'),
#         ('O', 'Otro'),
#     ]

#     STATUS_CHOICES = [
#         ('activo', 'Activo'),
#         ('inactivo', 'Inactivo'),
#     ]
    
#     ROLE_CHOICES = [
#         ('admin', 'Administrador'),
#         ('user', 'Usuario'),
#     ]

#     username = models.CharField(max_length=255, unique=True)
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)
#     correo = models.EmailField(unique=True)
#     telefono = models.CharField(max_length=20)
#     genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     rol = models.CharField(max_length=10, choices=ROLE_CHOICES)
#     estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='activo')
#     password = models.CharField(max_length=255)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['nombre', 'apellido', 'correo']

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Asegura que la contraseña esté hasheada
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    
    id = models.AutoField(primary_key=True)  # Este campo `id` será el identificador único
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'gender', 'role']

    def __str__(self):
        return self.email
