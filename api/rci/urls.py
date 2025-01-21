from rest_framework import routers
from django.urls import path, include

from .views import ASDI_LFPS_DisbursmentVoucherRecordViewSet

router = routers.DefaultRouter()
router.register(r'asdi-lfps-disbursment-voucher-record', ASDI_LFPS_DisbursmentVoucherRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]