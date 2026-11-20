from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from notes_app.serializers import RegisterSerializer,NotesSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notes_app.models import NotesDb,TaskDb
 

# Create your views here.
class RegistrationView(APIView):
    def post(self,request):
        serializer_instance=RegisterSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "message":"Registration Successfull"
            })
        else:
            return Response(data=serializer_instance.errors)
        
class NotesListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        notes=NotesDb.objects.filter(user=request.user)
        serializer_instance=NotesSerializer(notes,many=True)
        return Response(serializer_instance.data)
    
    def post(self,request):
        serializer_instance=NotesSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        
class NotesRetrieveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,pk):
        note_object=get_object_or_404(NotesDb,id=pk)
        if note_object.user==request.User:
            serializer_instance=NotesSerializer.request.user
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        
    def put(self,request,pk):
        note_object=get_object_or_404(NotesDb,id=pk,user=request.user)
        serializer_instance=NotesSerializer(note_object,data=request.user)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        return Response(serializer_instance.errors)
    
    def delete(self,request,pk):
        note_object=get_object_or_404(NotesDb,id=pk,user=request.user)
        note_object.delete()
        return Response({
            "message":"deleted successfully"
        })
        
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
        request.user.auth_token.delete()
        return Response({
            "message":"logout success"
        })
        
class TaskListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        task=TaskDb.objects.filter(user=self.request.user)
        serializer_instance=TaskSerializer(task,many=True)
        return Response(serializer_instance.data)
    
    
    def post(self,request):
        serializer_instance=TaskSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
    
    
class TaskRetrieveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        task_object=get_object_or_404(TaskDb,id=pk)
        if task_object.user==request.User:
            serializer_instance=TaskSerializer.request.user
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        
    def put(self,request,pk):
        task_object=get_object_or_404(TaskDb,id=pk)
    
        
        
