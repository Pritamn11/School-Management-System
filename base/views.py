from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Student, Teacher
from .serializers import UserSerializer, StudentSerializer, TeacherSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class UserRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data.pop('user')  
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            student_data = request.data
            student_data['user'] = user.id 
            student_serializer = StudentSerializer(data=student_data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response({'message': 'Student registered successfully'}, status=status.HTTP_201_CREATED)
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data.pop('user')  
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            teacher_data = request.data
            teacher_data['user'] = user.id  
            teacher_serializer = TeacherSerializer(data=teacher_data)
            if teacher_serializer.is_valid():
                teacher_serializer.save()
                return Response({'message': 'Teacher registered successfully'}, status=status.HTTP_201_CREATED)
            return Response(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
        

        user = authenticate(email=email, password=password)
        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 200,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class StudentListView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()  # Get all students
        serializer = StudentSerializer(students, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherListView(APIView):
    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()  # Get all teachers
        serializer = TeacherSerializer(teachers, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)
    

