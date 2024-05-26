from rest_framework.decorators import api_view
from rest_framework.response import Response
from tecfood_admin.models import User
from tecfood_admin.serializers import UserSerializer
from tecfood_admin.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from  django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError



# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user=User.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        
        return Response({
                        'token': token.key,
                        'user':serializer.data}, 
                        status=status.HTTP_201_CREATED
                        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):

            token, created = Token.objects.get_or_create(user=user)

            serializer = UserSerializer(instance=user)

            return Response({
                            'token': token.key, 
                            'user': serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({
                             'error': 'Invalid password'}, 
                              status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response(
                        {'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = UserSerializer(instance=user)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    try:
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                           serializer.data,
                           status=status.HTTP_200_OK
                           )
        else:
            return Response(
                            serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                           )

    except ValidationError as e:
        return Response(
                        {'error': str(e)}, 
                        status=status.HTTP_400_BAD_REQUEST
                        )
    except Exception as e:
        return Response(
                       {'error': str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                        )
        
        
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)