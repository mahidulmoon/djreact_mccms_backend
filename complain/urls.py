from django.urls import path,include
from rest_framework import routers
from .views import ComplainViewSet,ComplainPostViewSet

router = routers.DefaultRouter()
router.register('complains',ComplainViewSet)
router.register('postcomplain',ComplainPostViewSet)

urlpatterns = [
    path('',include(router.urls)),
]