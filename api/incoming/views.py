from rest_framework import permissions, viewsets
from .serializers import IARSerializer, POSerializer
from .models import IARRecord, PORecord
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import logging


# Create your views here.
class IARRecordViewSet(viewsets.ModelViewSet):
    queryset = IARRecord.objects.all()
    serializer_class = IARSerializer
    permission_classes = [permissions.AllowAny]
    


class IARRecordCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        logging.debug("POST request received")
        serializer = IARSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class IARRecordUpdateView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def put(self, request, *args, **kwargs):
#         logging.debug("PUT request received")
#         instance = IARRecord.objects.get(pk=kwargs['pk'])
#         serializer = IARSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PORecordViewSet(viewsets.ModelViewSet):
    queryset = PORecord.objects.all()
    serializer_class = POSerializer
    permission_classes = [permissions.AllowAny]

    

class PORecordCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        logging.debug("POST request received")
        serializer = POSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)