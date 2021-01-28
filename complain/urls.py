from django.urls import path,include
from rest_framework import routers
from .views import ComplainViewSet

router = routers.DefaultRouter()
router.register('complains',ComplainViewSet)

urlpatterns = [
    path('',include(router.urls)),
]