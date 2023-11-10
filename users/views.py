from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, EditSerializer
from django.contrib.auth.models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        print("hit")
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

def get_user(token):
    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    return payload['id']

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        user = User.objects.filter(id=get_user(token)).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class EditUserView(APIView):
    def put(self, request):
        token = request.COOKIES.get('jwt')
        user_id = get_user(token)
        user_data = request.data
        User.objects.filter(id=user_id).update(**user_data)
        return Response({
            "status":"200",
            "message":"profile Update successfully"
        })

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


