from django.urls import path,include
from rest_framework import routers
from .views import ComplainViewSet,ComplainPostViewSet,ComplainRatingViewSet

router = routers.DefaultRouter()
router.register('complains',ComplainViewSet)
router.register('postcomplain',ComplainPostViewSet)
router.register('ratecomplain',ComplainRatingViewSet)

urlpatterns = [
    path('',include(router.urls)),
]