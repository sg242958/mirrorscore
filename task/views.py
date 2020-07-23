from django.shortcuts import render
from .models import Student
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from .serializers import StudentSerializer

class StudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer

class StudentList(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]