from rest_framework import permissions, viewsets
from .serializers import IARSerializer
from .models import IARRecord
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class IARRecordViewSet(viewsets.ModelViewSet):
    queryset = IARRecord.objects.all()
    serializer_class = IARSerializer
    permission_classes = [permissions.AllowAny]
    


class IARRecordCreateView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = IARSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)