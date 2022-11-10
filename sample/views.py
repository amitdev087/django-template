from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentsSerializers  
from django.shortcuts import get_object_or_404  

# Create your views here.


class StudentView(APIView):
    # Get All Objects
    # def get(self, request, *arga,**kwarga):
    #     result=Students.objects.all()
    #     serializers=StudentsSerializers(result,many=True)
    #     return Response({'status':'success',"students":serializers.data},status=200)

    def get(self,request,id):
        result=Students.objects.get(id=id)
        if id:
            serializer=StudentsSerializers(result)
            return Response({'stutus':'success','student':serializer.data},status=200)

        result=Students.objects.all()
        serializer=StopAsyncIteration(result)
        return Response({'status':'sucess','students':serializer.data},status=200)

    def post(self,request):
        seriliazer=StudentsSerializers(data=request.data)
        if(seriliazer.is_valid()):
            seriliazer.save()
            return Response({'status':'success',"data":seriliazer.data},status=status.HTTP_200_OK)

        else:
            return Response({'status':'errors',"data":seriliazer.errors},status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,id):
        result=Students.objects.get(id=id)
        serializer=StudentsSerializers(result,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})

        else:
            return Response({'status':'success','data':serializer.errors})

    def delete(self,request,id=None):
        result=get_object_or_404(Students,id=id)
        result.delete()
        return Response({'status':'success','data':"record deleted"})

