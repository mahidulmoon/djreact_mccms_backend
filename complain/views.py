from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Complain_table,Ratings
from .serializers import ComplainSerializer,ComplaineRatingSerializer,StatusUpdateSerializer
from .pagination import NumberOfComplain
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser,SAFE_METHODS
from rest_framework.decorators import api_view,permission_classes,authentication_classes

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin


# Create your views here.
@api_view(['PUT'])
@permission_classes([IsAdminUserOrReadOnly, ])
@authentication_classes([TokenAuthentication, ])
def statusUpdateViewSet(request,pk):
    try: 
        snippet = Complain_table.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = StatusUpdateSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain_table.objects.all().order_by('-created_at')
    serializer_class = ComplainSerializer
    pagination_class = NumberOfComplain
    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ComplainPostViewSet(viewsets.ModelViewSet):
    queryset = Complain_table.objects.all()
    serializer_class = ComplainSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)

    def list(self,request):
        queryset = Complain_table.objects.filter(complainer_email=request.user.email)
        serializer = ComplainSerializer(queryset,many=True)
        return Response(serializer.data)



class ComplainRatingViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = ComplaineRatingSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)





# class StatusUpdateViewSet(viewsets.ModelViewSet):
#     queryset = Complain_table.objects.all()
#     serializer_class = StatusUpdateSerializer
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = (IsAdminUserOrReadOnly,)

