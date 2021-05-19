from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CoverNewz
from .serializers import CoverNewzSerializer

@api_view(['GET'])
def CoverNewzList(request):
    if request.method == 'GET':
        snippets = CoverNewz.objects.all()
        serializer = CoverNewzSerializer(snippets, many=True)
        return Response(serializer.data)