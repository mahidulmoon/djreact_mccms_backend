from rest_framework.pagination import PageNumberPagination

class ListPagination(PageNumberPagination):
    page_size = 3   #object per page