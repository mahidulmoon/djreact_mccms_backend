from django.urls import path,include
from rest_framework import routers
from .views import UserProfileViewSet,PreviligedUser


router = routers.DefaultRouter()
router.register('registeruser',UserProfileViewSet)
router.register('previligeduser',PreviligedUser)


urlpatterns = [
    path('',include(router.urls)),
]