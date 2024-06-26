from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            return None
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        except jwt.ImmatureSignatureError:
            raise AuthenticationFailed('Token is not yet valid (iat)')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        
        return (user, None)
