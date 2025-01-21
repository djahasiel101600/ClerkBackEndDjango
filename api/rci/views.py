from rest_framework import permissions, viewsets
from .serializers import RCISerializer
from .models import ASDI_LFPS_DisbursmentVoucherRecord

class ASDI_LFPS_DisbursmentVoucherRecordViewSet(viewsets.ModelViewSet):
    queryset = ASDI_LFPS_DisbursmentVoucherRecord.objects.all()
    serializer_class = RCISerializer
    permission_classes = [permissions.AllowAny]