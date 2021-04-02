from django.urls import path,include
from rest_framework import routers
from .views import UserProfileViewSet,PreviligedUser,CustomObtainAuthToken,adminDashShort


router = routers.DefaultRouter()
router.register('registeruser',UserProfileViewSet)
router.register('previligeduser',PreviligedUser)


urlpatterns = [
    path('',include(router.urls)),
    path('login',CustomObtainAuthToken.as_view()),
    path('admindashshort',adminDashShort),
]