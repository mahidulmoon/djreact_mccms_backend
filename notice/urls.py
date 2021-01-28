from rest_framework import routers
from .views import NoticeViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register('notices',NoticeViewSet)


urlpatterns = [
    path('',include(router.urls)),
]