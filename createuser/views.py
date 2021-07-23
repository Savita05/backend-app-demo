# from django.shortcuts import render, render_to_response
import createuser
from django.db import models
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from createuser.models import ProjectFiles
from createuser.serializers import UpdateSerializer
from rest_framework import status
from .models import upload_path, userprofile, assignTaskFiles, loginprofile, objectLevel, SceneLevel, ProjectFiles, Objectcategories
from .serializers import UpdateSerializer, ObjectcategoriesSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from createuser import serializers
from django.core.files.storage import default_storage
from django.core.files import File
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django import forms
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class RegisterUser(APIView):   
    def post(self, request):
        print (request.data)
        obj = loginprofile()  # gets new object  
        obj.firstName = request.data['firstName']
        obj.role = request.data['role']
        obj.password = request.data['password']
        obj.save()
        return Response('sucesssfully')

class Login(APIView):
    def post(self, request):
        cred=request.data
        name=request.data['firstName']
        password=request.data['password']
        #role=request.data['role']
        print("cred",cred)
        check=loginprofile.objects.filter(firstName=name,password=password).values()
        if check:  
            result = {
                'status': '200', 
                'message': 'Login Successfull'
            }
            return JsonResponse(result)
        
        # elif (check != ("/^[0-9]") ):
        #     print("enetering elif loop")
        #     result = {'status': '401', 
        #         'message': 'invalid inputs'          
        #     }
        #     return JsonResponse(result)

        elif not check:
            return  Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)
        
class Getuser(APIView):
    def get(self, request):
        print (request.data)
        entry = loginprofile.objects.all().values()
        print("entry",entry)
        return Response(entry)

class TaskFiles(APIView):
     def post(self, request):
        print (request.data)
        obj = assignTaskFiles()  # gets new object
        obj.File_Name = request.data['File_Name']
        obj.project_name = request.data['project_name']
        obj.Task_level = request.data['Task_level']
        obj.Priority = request.data['Priority']
        obj.Created_Date = request.data['Created_Date']
        obj.status = request.data['status']
        obj.Action = request.data['Action']
        obj.save()
        return Response('sucesssfull')

class ObjectLevel(APIView):   
    def post(self, request):
        print (request.data)
        obj = objectLevel() 
        obj.trackId = request.data['trackId']
        obj.objectClass = request.data['objectClass']
        obj.pose = request.data['pose']
        obj.occlusion = request.data['occlusion']
        obj.lane_change = request.data['lane_change']
        obj.breakLight = request.data['breakLight']
        obj.save()
        return Response('sucesssfull')

class SceneLevelQuery(APIView):   
    def post(self, request):
        print (request.data)
        obj = SceneLevel() 
        obj.Light_Condition = request.data['Light_Condition']
        obj.Road_Type = request.data['Road_Type']
        obj.Road_works = request.data['Road_works']
        obj.Tunnel = request.data['Tunnel']
        obj.Weather = request.data['Weather']
        obj.Street_Condition = request.data['Street_Condition']
        obj.save()
        return Response('sucesssfull')


class GetObjectLevel(APIView):
    def get(self, request):
            values1 = objectLevel.objects.all().values()
            print(values1)
            return Response(values1)

class GetSceneLevel(APIView):
    def get(self, request):    
            values1 = SceneLevel.objects.all().values()
            print(values1)
            return Response(values1)


class AddProjectFiles(APIView):
     def post(self, request):
        project_F= request.data['project_Feature']
        tool_v= request.data['Tool_version']
        feature_without=str(project_F)[1:-1]
        tool_without=str(tool_v)[1:-1]
        obj = ProjectFiles()  # gets new object
        obj.project_name = request.data['project_name']
        obj.project_Feature =feature_without
        obj.Tool_version = tool_without 
        obj.save()
        return Response('sucesssfull')
        

class GetTaskFilesList(APIView):
    def get(self, request):
            print (request.data)
            entry = assignTaskFiles.objects.all().values()
            return Response(entry)

class GetAllProjectsDetails(APIView):
    def get(self, request):
            print (request.data)
            entry = ProjectFiles.objects.all().values()
            return Response(entry)


class GetProjectName(APIView):
    def get(self, request):
        entry = ProjectFiles.objects.values("project_name")
        return Response(entry)


@api_view(['GET', 'PUT', 'DELETE'])
def getProjectDetails(request, project_name):
    if request.method == 'GET':
       projectdetails = ProjectFiles.objects.all()
       projectName = request.GET.get('project_name', None)
       print("projectname",projectName)
       filteredList = projectdetails.filter(project_name=projectName).values()
       #print("filtered list",filteredList)
       return Response(filteredList)

@api_view(['GET', 'PUT', 'DELETE'])
def gettasksfilteredonProjects(request, project_name):
    if request.method == 'GET':
        projectdetails = assignTaskFiles.objects.all()
        projectName = request.GET.get('project_name', None)
        print("projectfilestask", projectName)
        listing = projectdetails.filter(project_name=projectName).values()
        #print(listing)
        return Response(listing)




class UserRoles(APIView):
     def get(self, request):
         list = loginprofile.objects.values("role")
         print("list of roles" ,list)
         if(loginprofile.objects.values("role") == "maker"):
             return Response(list)



class Deleterecords(APIView):
    def delete(self, request):
            print (request.data)
           # firstName = request.data['firstName']
            loginprofile.objects.all().delete()
            print (request.data)
            return Response("deleted sucesssfull")


class Updateuser(APIView):
    def put(self, request):
        obj = loginprofile()
        id = request.data['id']
        loginprofile.objects.filter(id=id).update(firstName=request.data['firstName'],
        password=request.data['password'])
        loginprofile.objects.filter(id=id).update()
        obj.save()
        details = userprofile.objects.filter(id=id)
        serializer = UpdateSerializer(details,id)    
        return Response("Updated")
        print("*********",serializer.errors)


@api_view(['GET', 'POST', 'DELETE'])
def getobjectCategories(request):
    if request.method == 'POST':
        obj = Objectcategories() 
        obj.object_category = request.data['object_category']
        obj.save() 
        return Response("Saved successfully")
        
    elif request.method == 'GET':
         categoryNames = Objectcategories.objects.all().values()
         return Response(categoryNames)

    else:
        request.method == 'DELETE'
        count = Objectcategories.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def getobjectCategories_id(request, pk):
    try: 
        categoryNames = Objectcategories.objects.get(pk=pk) 
    except Objectcategories.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        category_serializer = ObjectcategoriesSerializer(categoryNames) 
        return JsonResponse(category_serializer.data) 

    elif request.method == 'PUT': 
        cat_data = JSONParser().parse(request) 
        print(cat_data)
        category_serializer = ObjectcategoriesSerializer(categoryNames, data=cat_data) 
        if category_serializer.is_valid(): 
            category_serializer.save() 
            return JsonResponse(category_serializer.data) 
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        categoryNames.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
@csrf_exempt
def uploadimages(request, *args, **kwargs):
    print("request is ", request)
    title = request.POST.get('project_name')
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)  
    obj = assignTaskFiles()
    obj.File_Name = file
    obj.project_name = title
    obj.Task_level =  request.POST.get('Task_level')
    obj.Priority =  request.POST.get('Priority')
    obj.Created_Date =  request.POST.get('Created_Date')
    obj.status = request.POST.get('status')
    obj.Action =  request.POST.get('Action')
    obj.save()
    return JsonResponse(file_name,safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def getAnnotationImageFile(request, File_Name, project_name):
    if request.method == 'GET':
        projectdetails = assignTaskFiles.objects.all()
        projectName = request.GET.get('project_name')
        filename = request.GET.get('File_Name')
        print("projectname", projectName)
        print("filename", filename)
        fetchfileandProjectName = projectdetails.filter(project_name=projectName, File_Name=filename).values()
        return Response(fetchfileandProjectName)