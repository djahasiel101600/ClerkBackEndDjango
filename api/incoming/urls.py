from rest_framework import routers
from django.urls import path, include

from .views import IARRecordViewSet
from .views import IARRecordCreateView
from .views import PORecordViewSet
from .views import PORecordCreateView

router = routers.DefaultRouter()
router.register(r'iar-record', IARRecordViewSet, basename='iar-record')
router.register(r'po-record', PORecordViewSet, basename='po-record')

urlpatterns = [
    path('',include(router.urls)),
    path('iar-record/', IARRecordViewSet.as_view({'get': 'list'}), name='iar-record-list'),
    path('iar-record/create/', IARRecordCreateView.as_view(), name='iar-record-create'),
    path('po-record/', PORecordViewSet.as_view({'get': 'list'}), name='po-record-list'),
    path('po-record/create/', PORecordCreateView.as_view(), name='po-record-create'),
]