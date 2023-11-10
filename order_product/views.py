from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from users.views import get_user
from django.contrib.auth.models import User
from .models import OrderItem, Item
from django.http import HttpResponse
from rest_framework import status
# from .serializers import OrderSerializer

class OrderItemView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        try:
            user = get_user(token)
        except:
            raise AuthenticationFailed('user not login')
        response = Response()
        response.data = OrderItem.objects.filter(user_id = int(user)).values()
        return Response(response.data, status=status.HTTP_200_OK)

    def post(self, request):
        token = request.COOKIES.get('jwt')
        try:
            user_id = get_user(token)
        except:
            raise AuthenticationFailed('user not login')
        requ = request.data
        requ['user_id'] = user_id
        OrderItem.objects.create(**requ)
        response = Response()
        response.data = {
            'status': '200',
            'message': 'Item created Successfully',
        }
        return Response(response.data, status=status.HTTP_200_OK)


class ItemView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        try:
            user_id = get_user(token)
        except:
            raise AuthenticationFailed('user not login')
        print(user_id)
        response = Response()
        response.data = Item.objects.all().values()
        return Response(response.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        token = request.COOKIES.get('jwt')
        try:
            user_id = get_user(token)
        except:
            raise AuthenticationFailed('user not login')

        requ = request.data
        Item.objects.create(**requ)

        response = Response()
        response.data = {
            'status': '200',
            'message': 'order created Successfully',
        }
        return Response(response.data, status=status.HTTP_200_OK)