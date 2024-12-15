"""
NOTE: youll need to use jwt tokens for login validations and the refresher to use the correct state manegement
TODO: you cannot define user links without calling these functions from the jwt tokens
therefore => 
# from rest_framework_simplejwt.tokens import RefreshToken
"""


def user_dashboard(request):    
    return render(request, 'user_dashboard.html')

from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Users
from .serializers import UserSerializer
from main.models import School
from django.contrib import messages

class RegisterView(APIView):
    def get(self, request):
        schools = School.objects.order_by('name')
        return render(request, "register.html", {'schools': schools})

    def post(self, request):
        data = request.POST.copy() 
        data['password'] = make_password(data['password'])

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('/user/login')
        else:
            schools = School.objects.order_by('name')
            return render(request, "register.html", {'schools': schools, 'errors': serializer.errors})
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
        # print(password)

        user = authenticate(request, username=username, password=password)
        print(password) # for debugging the password
        if user and user.check_password(password):
         
            refresh = RefreshToken.for_user(user)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid Username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    def get(self, request): 
        return render(request, "login.html")
 

def explore(request):
    return render(request, "explore.html")

def schoolhome(request):
    return render(request, "course.html")