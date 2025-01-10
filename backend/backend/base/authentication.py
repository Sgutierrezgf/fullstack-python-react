from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get('access_token')
        print(f"Token recibido: {access_token}")

        if not access_token:
            raise AuthenticationFailed('No token provided')

        try:
            # Intentamos validar el token
            validated_token = self.get_validated_token(access_token)
            print(f"Token validado: {validated_token}")
            user = self.get_user(validated_token)
        except Exception as e:
            print(f"Error al validar el token: {str(e)}")
            raise AuthenticationFailed('Token is invalid or expired')

        return (user, validated_token)