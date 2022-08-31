from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

# Create your views here

class StudentViewSet(viewsets.ViewSet):
    #To GET data(list)
    def list(self, request):
        print("\n<<<<<<<<<<<<<<<<< list/GET >>>>>>>>>>>>>>>>>")
        print("Basename : ", self.basename)
        print("Action :", self.action) #Action is very important!!(main task in upcoming projects is performed by Action!!)
        print("Detail :", self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data)


    #To POST data
    def create(self, request):
        print("\n<<<<<<<<<<<<<<<<< create/POST >>>>>>>>>>>>>>>>>")
        print("Basename : ", self.basename)
        print("Action :", self.action) #Action is very important!!(main task in upcoming projects is performed by Action!!)
        print("Detail :", self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Inserted Successfully!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #To GET specific data(retrive)
    def retrieve(self, request, pk=None):#To GET specific data we have to use this url on postman [http://127.0.0.1:8000/stucreate/9/]
        print("\n<<<<<<<<<<<<<<<<< retrieve/GET(specific data) >>>>>>>>>>>>>>>>>")
        print("Basename : ", self.basename)
        print("Action :", self.action) #Action is very important!!(main task in upcoming projects is performed by Action!!)
        print("Detail :", self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)


    #To PUT data
    def update(self, request, pk): #to PUT data we have to use this url on postman [http://127.0.0.1:8000/stucreate/9/]
        print("\n<<<<<<<<<<<<<<<<< update/PUT >>>>>>>>>>>>>>>>>")
        print("Basename : ", self.basename)
        print("Action :", self.action) #Action is very important!!(main task in upcoming projects is performed by Action!!)
        print("Detail :", self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Updated Successfully!!!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #To PATCH data
    def partial_update(self, request, pk): #to PATCH data we have to use this url on postman [http://127.0.0.1:8000/stucreate/9/]
        print("\n<<<<<<<<<<<<<<<<< partial_update/PATCH >>>>>>>>>>>>>>>>>")
        print("Basename : ", self.basename)
        print("Action :", self.action) #Action is very important!!(main task in upcoming projects is performed by Action!!)
        print("Detail :", self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Updated Successfully(Partially)!!!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #To DELETE data
    def destroy(self, request, pk): #to DELETE data we have to use this url on postman [http://127.0.0.1:8000/stucreate/9/]
        print("\n<<<<<<<<<<<<<<<<< destroy/DELETE >>>>>>>>>>>>>>>>>")
        print("Basename : ", self.basename)
        print("Action :", self.action) #Action is very important!!(main task in upcoming projects is performed by Action!!)
        print("Detail :", self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg' : 'Data Deleted Successfully!!!'})










#PROJECT gs13

# from . models import Student
# from .serializers import StudentSerializer
# from rest_framework.generics import ListCreateAPIView #Type of Concrete View Classes
# from rest_framework.generics import RetrieveUpdateDestroyAPIView #Type of Concrete View Classes

# # Create your views here


# #To GET all data(List)   and   To POST data(Create)
# class StudentListCreate(ListCreateAPIView): #pk(primary key is not required)
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# #To GET specific data(Retrieve)   and   To PUT/PATCH data(Update)   and   To DELETE data(Destroy)
# class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView): #pk(Primary key is required)
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer