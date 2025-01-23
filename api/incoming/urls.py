from rest_framework import routers
from django.urls import path, include

from .views import IARRecordViewSet
from .views import IARRecordCreateView
from .views import PORecordViewSet
from .views import PORecordCreateView

router = routers.SimpleRouter()
router.register(r'iar-record', IARRecordViewSet)
router.register(r'po-record', PORecordViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('iar-record/viewlist/', IARRecordViewSet.as_view({'get': 'list'}), name='iar-record-list'),
    # path('iar-record/create/', IARRecordCreateView.as_view(), name='iar-record-create'),
    # path('po-record/viewlist/', PORecordViewSet.as_view({'get': 'list'}), name='po-record-list'),
    # path('po-record/create/', PORecordCreateView.as_view(), name='po-record-create'),
]