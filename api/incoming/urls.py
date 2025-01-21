from rest_framework import routers
from django.urls import path, include

from .views import IARRecordViewSet
from .views import IARRecordCreateView

router = routers.DefaultRouter()
router.register(r'iar-record', IARRecordViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('iar-record/create/', IARRecordCreateView.as_view(), name='iar-record-create'),
]