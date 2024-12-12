from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

"""
NOTE: youll need to use jwt tokens for login validations and the refresher to use the correct state manegement
TODO: you cannot define user links without calling these functions from the jwt tokens
therefore => 
# from rest_framework_simplejwt.tokens import RefreshToken
"""
from django.contrib.auth.hashers import make_password
from .models import Users
from .serializers import UserSerializer




def user_dashboard(request):    
    return render(request, 'user_dashboard.html')


class AccountViw (APIView):
    print("Hello world")

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        data['password'] = make_password(data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SIgnUpView(APIView):
    print("hello world")

# '''
# For views that we might take seriously later along the line 
# '''
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

# class ProtectedView(APIView):
#     authentication_classes = [JWTAuthentication]  # Use JWT Authentication
#     permission_classes = [IsAuthenticated]  # Require authentication

#     def get(self, request):
#         content = {'message': 'hehehe login first'}
#         return Response(content)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = Users.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


def explore(request):
    return render(request, "explore.html")

def schoolhome(request):
    return render(request, "course.html")