from .models import User
from main.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from .tokens import *


@api_view(['POST'])
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                token = get_token_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': token,
                }
            else:
                status = 403
                message = "Invalid Password or Username !"
                data = {
                    'status': status,
                    'message': message
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined !'
            data = {
                'status': status,
                'message': message
            }

        return Response(data)
    except Exception as err:
            return Response(f'{err}')



@api_view(['POST'])
def singup_view(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        new = User.objects.create_user(
            username=username,
            passwor=password,
            phone_number=phone_number,
        )
        ser = UserSerializer(new)
        return Response(ser.data)
    except Exception as err:
        return Response(f'{err}')




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data': 'sucses'})




@api_view(['PUT'])
def edit_user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.POST.get('username')
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            user.username = username
            user.phone_number = phone_number
            if password is not None:
                user.set_password(password)
                user.save()
                ser = UserSerializer(user)
                return Response(ser.data)
        except:
            status = 404
            message = 'Request failed'
            data = {
                'status': status,
                'message': message
            }
    except:
        status = 404
        message = 'User not found'
        data = {
            'status': status,
            'message': message
        }
    return Response(data)




@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        data = {
            'message': "User deleted successfully"
        }
        return Response(data)
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
        return Response(data)




